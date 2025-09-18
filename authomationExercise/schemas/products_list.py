get_all_products_list = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "responseCode": {
      "type": "number"
    },
    "products": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "number"
          },
          "name": {
            "type": "string"
          },
          "price": {
            "type": "string"
          },
          "brand": {
            "type": "string"
          },
          "category": {
            "type": "object",
            "properties": {
              "usertype": {
                "type": "object",
                "properties": {
                  "usertype": {
                    "type": "string"
                  }
                },
                "required": [
                  "usertype"
                ]
              },
              "category": {
                "type": "string"
              }
            },
            "required": [
              "usertype",
              "category"
            ]
          }
        },
        "required": [
          "id",
          "name",
          "price",
          "brand",
          "category"
        ]
      }
    }
  },
  "required": [
    "responseCode",
    "products"
  ]
}
