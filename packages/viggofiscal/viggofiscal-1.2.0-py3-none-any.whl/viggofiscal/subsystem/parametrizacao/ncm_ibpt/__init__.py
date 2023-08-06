from viggocore.common import subsystem
from viggofiscal.subsystem.parametrizacao.ncm_ibpt \
    import resource, controller, router

subsystem = subsystem.Subsystem(resource=resource.NcmIbpt,
                                controller=controller.Controller,
                                router=router.Router)