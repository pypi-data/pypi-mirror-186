<h1>Rule Example</h1>

<p>
{
  "_id": {
  },
  "created_at": {
  },
  "updated_at": {
  },
  "deleted_at": None,
  "uuid": str,
  "version": int,
  "steps": [
    {
      "component": str,
      "path_component": str,
      "alias": str,
      "active": bool,
      "settings": dict
    },
    {
      "component": str,
      "path_component": str,
      "alias": str,
      "active": bool,
      "settings": {}
    },
    {
      "component": str,
      "path_component": str,
      "alias": str,
      "active": bool,
      "settings": {
        "data_from_component": str,
        "environment_variable": "${ENVIRONMENT_VARIABLE}",
      }
    }
 ],
  "on_stop": [],
  "on_error": []
}</p>