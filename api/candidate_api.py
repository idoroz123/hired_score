from flask import Blueprint, json, request

from api.utils import format_experience, get_candidates_json, get_linked_in_url, read_candidates_csv_file



candidate_api = Blueprint("canditates", __name__)


@candidate_api.route("/all", methods=["GET"])
def list_candidates():
    try:
        res = []
        canditates_json = get_candidates_json()
        # candidates_csv = read_candidates_csv_file()

        for candidate in canditates_json:
            candidate_name = candidate.get("contact_info", {}).get("name", {}).get("formatted_name")
            candidate_experience = format_experience(candidate.get("experience", {}))
            res.append({"name": candidate_name, "experience": candidate_experience})
                


        return json.dumps({"results": res, "status_code":200})

    except Exception as e:
        raise Exception(
            f"An error occurred while fetching candidates: {str(e)}", status_code=500
        )

