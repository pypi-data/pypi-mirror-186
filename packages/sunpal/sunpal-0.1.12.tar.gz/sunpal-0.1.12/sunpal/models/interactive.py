from sunpal.model import Model
from sunpal import request


class Interactive(Model):
    class Signature(Model):
        fields = ["id", "signature", "created"]

    class DataSheet(Model):
        fields = ["id", "archive", "name", "type"]

    class Documment(Model):
        fields = ["id", "name", "document_reference_id"]

    class ViewData(Model):
        fields = ["id", "is_mobile", "device_family"]

    fields = [
        "id",
        "project_name",
        "has_permalink",
        "has_approbed",
    ]

    @staticmethod
    def create(params=None, env=None, headers=None):
        return request.send(
            "post", request.uri_path("proposals/interactive"), params, env, headers
        )

    @staticmethod
    def retrieve(id, params=None, env=None, headers=None):
        return request.send(
            "get", request.uri_path("proposals/interactive", id), params, env, headers
        )

    @staticmethod
    def update(id, params=None, env=None, headers=None, file=None):
        return request.send(
            "patch",
            request.uri_path("proposals/interactive", id),
            params,
            env,
            headers,
            file,
        )

    @staticmethod
    def delete(id):
        return request.send("delete", request.uri_path("proposals/interactive", id))

    @staticmethod
    def retrieve_signature(id, params=None, env=None, headers=None):
        return request.send(
            "get", request.uri_path("proposals/signature", id), params, env, headers
        )

    @staticmethod
    def retrieve_datasheets(params=None, env=None, headers=None):
        return request.send(
            "get", request.uri_path("proposals/datasheets"), params, env, headers
        )

    @staticmethod
    def add_datasheet(params=None, env=None, headers=None, file=None):
        return request.send(
            "post", request.uri_path("proposals/datasheets"), params, env, headers, file
        )

    @staticmethod
    def delete_datasheet(id, params):
        return request.send(
            "delete", request.uri_path("proposals/datasheets", id), params
        )

    @staticmethod
    def retrieve_documments(params=None, env=None, headers=None):
        return request.send(
            "get", request.uri_path("proposals/documments"), params, env, headers
        )

    @staticmethod
    def add_documment(params=None, env=None, headers=None, file=None):
        return request.send(
            "post", request.uri_path("proposals/documments"), params, env, headers, file
        )

    @staticmethod
    def delete_documment(id, params):
        return request.send(
            "delete", request.uri_path("proposals/documments", id), params
        )

    @staticmethod
    def delete_documment_by_reference(id):
        return request.send(
            "delete", request.uri_path("proposals/documment-reference", id)
        )

    @staticmethod
    def remove_approbal(id):
        return request.send("delete", request.uri_path("proposals/approbed", id))

    @staticmethod
    def revoke_signature(id):
        return request.send("delete", request.uri_path("proposals/signature", id))

    @staticmethod
    def retrieve_views(id=None, env=None, headers=None):
        return request.send(
            "get", request.uri_path("proposals/views", id), None, env, headers
        )

    @staticmethod
    def restart_views(id):
        return request.send("delete", request.uri_path("proposals/restartviews", id))
