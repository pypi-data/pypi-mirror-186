_liepoly_name = 'liepoly'
_lieoperator_name = 'lieop'
_lexp_name = 'lexp'

# isinstance/type checking becomes unreliable if re-loading code interactively. therefore we introduce small
# helper checks
def _isobj(name: str, *objs):
    return all([name == getattr(obj, '_name', None) for obj in objs])
