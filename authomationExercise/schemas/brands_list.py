get_all_brands_list = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "responseCode": {
      "type": "number"
    },
    "brands": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "number"
          },
          "brand": {
            "type": "string"
          }
        },
        "required": [
          "id",
          "brand"
        ]
      }
    }
  },
  "required": [
    "responseCode",
    "brands"
  ]
}