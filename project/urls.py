import flask, main_app

main_app.app.add_url_rule(rule = '/', view_func = main_app.render_main)
