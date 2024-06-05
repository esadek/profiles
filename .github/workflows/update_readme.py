import os
import yaml

directory = os.path.dirname(__file__) + "/../../"

def generate_header(text: str, size: int) -> str:
    return f"{'#' * size} {text}\n\n"

def generate_table(column_names: list[str], rows: list[list[str]]) -> str:
    table_head = f"<thead>\n<tr><th>{'</th><th>'.join(column_names)}</th></tr>\n</thead>"
    table_body = "\n<tbody>\n"
    for row in rows:
        table_body += f"<tr><td>{'</td><td>'.join(row)}</td></tr>\n"
    table_body += "</tbody>\n"
    return f"<table>\n{table_head}{table_body}</table>"

def get_entities() -> str:
    with open(directory + "pb_project.yaml") as f:
        try:
            project = yaml.safe_load(f)
            document = ""
            document += generate_header(project.get("name"), 1)
            document += generate_header("Entities", 2)
            columns = ["Entity", "ID Stitcher", "ID Types"]
            entities = project.get("entities")
            rows = []
            for entity in entities:
                rows.append([
                    entity.get("name"),
                    entity.get("id_stitcher"),
                    ', '.join(entity.get("id_types"))
                ])
            document += generate_table(columns, rows)
            document += "\n\n"
        except yaml.YAMLError as exc:
            print(exc)
    return document

def get_id_types() -> str:
    with open(directory + "pb_project.yaml") as f:
        try:
            project = yaml.safe_load(f)
            document = ""
            document += generate_header("ID Types", 2)
            columns = ["ID Types", "Filters"]
            filter_columns = ["Type", "Value", "Regex"]
            id_types = project.get("id_types")
            rows = []
            for id_type in id_types:
                name = id_type.get("name")
                filters = id_type.get("filters")
                if filters:
                    for filter in filters:
                        filter_row = [list(map(str, [
                            filter.get("type"),
                            filter.get("value", ""),
                            filter.get("regex", "")
                        ]))]
                    rows.append([
                        name,
                        generate_table(filter_columns, filter_row)
                    ])
                else:
                    rows.append([name, "None"])
            document += generate_table(columns, rows)
            document += "\n\n"
        except yaml.YAMLError as exc:
            print(exc)
    return document

def get_inputs() -> str:
    with open(directory + "models/inputs.yaml") as f:
        try:
            inputs = yaml.safe_load(f).get("inputs")
            document = ""
            document += generate_header("Inputs", 2)
            columns = ["Input", "Table", "IDs"]
            ids_columns = ["Entity", "Type", "Select"]
            rows = []
            for input in inputs:
                app_defaults = input.get("app_defaults")
                ids = app_defaults.get("ids")
                ids_rows = []
                for id in ids:
                    ids_rows.append(list(map(str, [
                        id.get("entity"),
                        id.get("type"),
                        f"<code>{id.get('select')}</code>"
                    ])))
                rows.append([
                    input.get("name"),
                    app_defaults.get("table"),
                    generate_table(ids_columns, ids_rows)
                ])
            document += generate_table(columns, rows)
            document += "\n\n"
        except yaml.YAMLError as exc:
            print(exc)
    return document

def get_models() -> str:
    with open(directory + "models/profiles.yaml") as f:
        try:
            models = yaml.safe_load(f).get("models")
            document = ""
            document += generate_header("Models", 2)
            columns = ["Model", "Type", "Entity"]
            rows = []
            for model in models:
                rows.append([
                    model.get("name"),
                    model.get("model_type"),
                    model.get("model_spec", {}).get("entity_key")
                ])
            document += generate_table(columns, rows)
            document += "\n\n"
        except yaml.YAMLError as exc:
            print(exc)
    return document

def get_var_groups() -> str:
    with open(directory + "models/profiles.yaml") as f:
        try:
            var_groups = yaml.safe_load(f).get("var_groups")
            document = ""
            document += generate_header("Var Groups", 2)
            columns = ["Var Group", "Entity"]
            rows = []
            for var_group in var_groups:
                rows.append([
                    var_group.get("name"),
                    var_group.get("entity_key")
                ])
            document += generate_table(columns, rows)
            document += "\n\n"
        except yaml.YAMLError as exc:
            print(exc)
    return document

def get_entity_vars() -> str:
    with open(directory + "models/profiles.yaml") as f:
        try:
            var_groups = yaml.safe_load(f).get("var_groups")
            document = ""
            document += generate_header("Var Groups", 2)
            columns = ["Entity Var", "Select", "From", "Where" ]
            rows = []
            for var_group in var_groups:
                for var in var_group.get("vars"):
                    entity_var = var.get("entity_var")
                    where = entity_var.get("where")
                    rows.append([
                        entity_var.get("name"),
                        f"<code>{entity_var.get('select')}</code>",
                        entity_var.get("from", ""),
                        f"<code>{where}</code>" if where else ""
                    ])
            document += generate_table(columns, rows)
            document += "\n\n"
        except yaml.YAMLError as exc:
            print(exc)
    return document

if __name__ == "__main__":
    document = get_entities()
    document += get_id_types()
    document += get_inputs()
    document += get_models()
    document += get_var_groups()
    document += get_entity_vars()
    with open(directory + "README.md", "w") as f:
        f.write(document)
