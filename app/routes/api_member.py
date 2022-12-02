from . import api_member

@api_member.route("/api/member", methods=["GET"])
def check_member():
    return {"ok":True}