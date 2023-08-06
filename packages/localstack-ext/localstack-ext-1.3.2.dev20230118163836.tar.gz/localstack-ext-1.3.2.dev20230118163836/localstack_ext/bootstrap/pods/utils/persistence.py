from typing import Any
import dill
def marshall_object(obj):return dill.dumps(obj)