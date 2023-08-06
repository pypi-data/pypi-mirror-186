from scinode.core.executor import Executor


class PropertyToSocket(Executor):
    """Out the properties as sockets."""

    def run(self):
        results = ()
        outputs = self.dbdata["outputs"]
        # all kwargs as one socket
        if len(outputs) == 1 and len(self.kwargs) != 1:
            return (self.kwargs,)
        # one kwarg as one socket
        # here we need to check
        for socket in outputs:
            results += (self.kwargs[socket["name"]],)
        return results


class ResultToSocket(Executor):
    """Out the result as sockets."""

    def run(self):
        import pickle

        db_results = pickle.loads(self.dbdata["results"])
        results = ()
        for result in db_results:
            results += (result["value"],)
        return results


def InputToSocket(*args):
    """Out the input as sockets."""
    results = ()
    for x in args:
        results += (x,)
    return results
