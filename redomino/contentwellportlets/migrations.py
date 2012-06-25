import logging

def from_2_1_to_3(context):
    context.runImportStepFromProfile('profile-redomino.contentwellportlets:default',
            'portlets')
    log = logging.getLogger("ContentWellPortlets")
    log.info("Ran portlets import step")
    
