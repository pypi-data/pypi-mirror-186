from notebook.utils import url_path_join
from notebook.base.handlers import AuthenticatedFileHandler, path_regex

class FileOrderHandler(AuthenticatedFileHandler):
    def get(self, path=''):
        # Path comes in with a leading slash, but changing the routing to put the slash
        # in the route breaks everything.  This strip is what Jupyter itself does.
        return super().get(url_path_join(path.strip('/'), '.custom_order'))

    def validate_absolute_path(self, root, absolute_path):
        # Disable the hidden file check of the AuthenicatedFileHandler by going up to
        # the tornado.web.StaticFileHandler.
        return super(AuthenticatedFileHandler, self).validate_absolute_path(root, absolute_path)

def load_jupyter_server_extension(nbapp):
    # In `jupyter notebook`, the root directory is in the `.notebook_dir` propery.
    # `jupyter server` has both, but notes that `.root_dir` is prefered, as
    # `notebook_dir` is deprecated.  Let's get ready for the future.
    root_dir = getattr(nbapp, 'root_dir', None)
    if root_dir is None:
        root_dir = getattr(nbapp, 'notebook_dir', '')
    route_pattern = url_path_join(nbapp.web_app.settings['base_url'], f'customorder{path_regex}')
    nbapp.web_app.add_handlers('.*$', [(route_pattern, FileOrderHandler, {'path': root_dir})])

# New name for Jupyter server
_load_jupyter_server_extension = load_jupyter_server_extension

# Configuration of the extensions
def _jupyter_server_extension_paths():
    return [{'module': 'jupytercustomsort'}]

def _jupyter_nbextension_paths():
    return [{
        'section': 'tree',
        'src': 'nbext',
        'dest': 'jupytercustomsort',
        'require': 'jupytercustomsort/main'
    }]
