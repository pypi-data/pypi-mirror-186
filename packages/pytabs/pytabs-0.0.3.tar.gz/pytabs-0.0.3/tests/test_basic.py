from context import pytabs

import pytabs.model

# substantiate pyTABS EtabsModel
etabs_model = pytabs.model.EtabsModel()


load_case_type = etabs_model.load_cases.static_nonlinear.set_case('nl_test')




# etabs_model.load_cases.static_nonlinear.set_geometric_nonlinearity('nl_test', etabs_model.load_cases.eGeometryNonlinearityTypes.P_DELTA)

# story_list = etabs_model.story.get_name_list()

# for story in story_list:
#     elevation = etabs_model.story.get_elevation(story_name=story)
#     height = etabs_model.story.get_height(story_name=story)
#     status = etabs_model.story.get_master_story(story_name=story)
#     similar_story = etabs_model.story.get_similar_to(story_name=story)
    
#     print(f"{story} | {height} | {elevation} |  {status} | {similar_story}")

# etabs_model.analysis_results.set_case_selected_for_output('Modal Eigen')

# etabs_model.analysis_results.set_mode_shape_setup(1, 5, True)

# mode_shape_setup = etabs_model.analysis_results.get_mode_shape_setup()

# print(mode_shape_setup)

# modal_period = etabs_model.analysis_results.modal_period()

# print(modal_period)

# etabs_model.analysis_results.set_case_selected_for_output('Self Weight')

# base_point = etabs_model.analysis_results.get_base_reaction_location()

# print(base_point)

# etabs_model.analysis_results.set_base_reaction_location((1.5, 2.3, 4.5))

# base_point = etabs_model.analysis_results.get_base_reaction_location()

# print(base_point)

# mvo = etabs_model.analysis_results.get_nonlinear_setup()
# print(mvo)

# mvo = etabs_model.analysis_results.set_nonlinear_setup('step-by-step')

# mvo = etabs_model.analysis_results.get_nonlinear_setup()
# print(mvo)