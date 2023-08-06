from functools import reduce
from hpc_suite.store import Store
from angmom_suite.basis import make_angmom_ops_from_mult, sf2ws
from angmom_suite.crystal import project_CF
from angmom_suite.multi_electron import Term
from .extractor import make_extractor


def make_evaluator(h_file, options):
    return ProjectCF(h_file, options)


class ProjectCF(Store):

    def __init__(self, h_file, options, units='cm^-1', fmt='% 20.13e'):

        self.h_file = h_file
        self.options = options

        # default to ground term/level if symbol is not suplied
        options['symbol'] = options['symbol'] or (
            options['ion'].ground_term if options['basis'] == 'l' else
            options['ion'].ground_level)

        description = \
            "Crystal field parameters of the {} {} in the {} basis.".format(
                str(options['symbol']),
                'level' if isinstance(options['symbol'], Term) else
                'multiplet',
                options['basis']
            )

        if options['ground']:
            description += \
                (" Warning: Only considering the {} lowest SO states "
                 "corresponding the ground {} {} of {}!").format(
                    reduce(lambda x, y: x * y,
                           options['symbol'].mult.values()),
                    str(options['symbol']),
                    'level' if isinstance(options['symbol'], Term) else
                    'multiplet',
                    str(options['ion'])
                )

        else:
            options['space'] = \
                options['space'] or options['ion'].casscf_terms('s')
            description += \
                " The input space spans the terms/levels: {}.".format(
                    ' '.join(map(str, options['space'])))

        # special case, remove cleaning up of input states all together
        if options['field'] == 0.0 and options['ener_thresh'] == 0.0:
            options['field'] = None
            description += " No pertubation of Kramers doublets."
        elif options['field'] == 0.0:
            description += " Kramers doublets are rotated into Jz eigenstates."
        else:
            description += (" Kramers doublets are split by a magnetic field "
                            "of {} mT.").format(options['field'])

        super().__init__('CFPs', description, label=(), units=units, fmt=fmt)

    def __iter__(self):

        smult = make_extractor(self.h_file, ("rassi", "spin_mult"))[()]
        soco = make_extractor(self.h_file, ("rassi", "SOS_coefficients"))[()]
        so_ener = make_extractor(self.h_file, ("rassi", "SOS_energies"))[()]

        try:
            sf_angm = make_extractor(self.h_file, ("rassi", "SFS_angmom"))[()]
            so_angm = soco.T.conj() @ sf2ws(sf_angm, smult) @ soco
        except KeyError:
            so_angm = make_extractor(self.h_file, ("rassi", "SOS_angmom"))[()]

        so_spin = soco.conj().T @ make_angmom_ops_from_mult(smult)[0:3] @ soco

        data = project_CF(so_ener, so_spin, so_angm, **self.options)[0]

        yield (self.format_label(), self.format_data(list(data.values())))
