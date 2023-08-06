from io import BytesIO
from multiprocessing import Pool

import zopfli
from django.contrib.staticfiles.storage import ManifestStaticFilesStorage
from django.contrib.staticfiles.utils import matches_patterns
from django.core.files.base import File
from psutil import cpu_count
from tqdm import tqdm


class GzipMixin:
    """
    Brings the Gzip-ability if mixed with a storage. Uses Zopfli for
    compression.

    Notes
    -----
    The base mixin was stolen from django-pipeline and then modified a lot
    https://django-pipeline.readthedocs.io/en/latest/storages.html
    """

    gzip_patterns = ("*.css", "*.js", "*.svg", "*.ttf")

    def _compress(self, original_file):
        c = zopfli.ZopfliCompressor(zopfli.ZOPFLI_FORMAT_GZIP)
        z = c.compress(original_file.read()) + c.flush()
        return File(BytesIO(z))

    def handle_file(self, path):
        """
        Handles a single path and generates the compressed file if required.
        It will create a .gz equivalent of that file.
        Parameters
        ----------
        path
            Path to the file to compress
        """

        if path:
            if not matches_patterns(path, self.gzip_patterns):
                return

            try:
                original_file = self.open(path, mode="rb")
            except FileNotFoundError:
                pass
            else:
                gzipped_path = "{0}.gz".format(path)

                if self.exists(gzipped_path):
                    self.delete(gzipped_path)

                gzipped_file = self._compress(original_file)
                gzipped_path = self.save(gzipped_path, gzipped_file)

                return gzipped_path, gzipped_path, True

    def post_process(self, paths, dry_run=False, **options):
        """
        For each path to post-process, potentially compress the files. That
        is done using a process pool that will parallelize the processing to
        speed it up.
        """

        super_class = super()

        if hasattr(super_class, "post_process"):
            for name, hashed_name, processed in super_class.post_process(
                paths.copy(), dry_run, **options
            ):
                if hashed_name != name:
                    paths[hashed_name] = (self, hashed_name)
                yield name, hashed_name, processed

        if dry_run:
            return

        cpus = (cpu_count(logical=False) or 1) + 1

        with Pool(processes=cpus) as pool:
            for out in tqdm(
                pool.imap_unordered(self.handle_file, paths),
                unit="file",
                total=len(paths),
            ):
                if out:
                    yield out


class GzipManifestStaticFilesStorage(GzipMixin, ManifestStaticFilesStorage):
    """
    Almost like the regular ManifestStaticFilesStorage, except it will create
    .gz files for all the text assets.
    """
