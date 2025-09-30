post_search_product = {
    "type": "object",
    "properties": {
        "responseCode": {
            "type": "integer"
        },
        "products": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer"
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
                                }
                            },
                            "category": {
                                "type": "string"
                            }
                        }
                    }
                }
            }
        }
    }
}