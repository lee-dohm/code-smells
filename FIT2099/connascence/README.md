# Connascence


## Connascence of name

* Multiple components must agree on the name of an entity. Method, class, parameters have names.

* If the name of a method changes, callers of that method must be changed to use the new name.

```python
class Request:

    def __init__(self, url, data=None, headers={},
                 origin_req_host=None, unverifiable=False,
                 method=None):
        pass

    def set_proxy(self, host, type):
        pass
```
> -- *[Connascenceio][connascenceIO]*

Changing the name of any part of this code will cause code that uses this class to break, including:

* Changing the class name from Request.
* Changing any of the method names (such as set_proxy).
* Changing the name of any of the parameters to either __init__ or set_proxy.

Connascence of name is unavoidable, since we refer to entities using labels. If we change the name of an entity when we declare it, we must also change all code that refers to that entity. For this reason, connascence of name is the **weakest*** connascence. 

However, it also illustrates how important it is to name entities in code well.

[connascenceIO]: https://www.connascence.io
