# swagger_spec.py

swagger_spec = {
    "swagger": "2.0",
    "info": {
        "title": "Flask Swagger API",
        "description": "API documentation for Flask Swagger API",
        "version": "1.0"
    },
    "paths": {
        "/add_item": {
            "post": {
                "summary": "Add an item",
                "description": "Endpoint to add an item",
                "parameters": [
                    {
                        "name": "data",
                        "in": "body",
                        "description": "Item data",
                        "required": True,
                        "schema": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "description": {"type": "string"},
                                "price": {"type": "number"},
                                "tax": {"type": "number"}
                            }
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Success"
                    }
                }
            }
        },
        "/get_items": {
            "get": {
                "summary": "Get all items",
                "description": "Endpoint to get all items",
                "responses": {
                    "200": {
                        "description": "Success"
                    }
                }
            }
        }
    }
}
