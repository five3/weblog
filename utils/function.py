def singleton(className):
    def wrapped():
        it =  className.__dict__.get('__it__')
        if it is not None:
            return it

        className.__it__=className()
        return className.__it__
    return wrapped

def model_to_object(model):
    t_list = []
    if model:        
        for line in model:
            t_list.append(dict(line))
    return t_list

def object_to_json(*object):
    import json
    return json.dumps(object)