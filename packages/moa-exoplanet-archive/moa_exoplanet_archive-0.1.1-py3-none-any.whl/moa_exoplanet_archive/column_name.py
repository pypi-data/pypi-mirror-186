try:
    from enum import StrEnum
except ImportError:
    from backports.strenum import StrEnum


class ColumnName(StrEnum):
    HJD = 'HJD'
    COR_FLUX = 'cor_flux'
    FLUX = 'flux'
    FLUX_ERR = 'flux_err'
    OBS_ID = 'obsID'
    JD = 'JD'
    FWHM = 'fwhm'
    SKY = 'sky'
    AIRMASS = 'airmass'
    NSTAR = 'nstar'
    SCALE = 'scale'
    EXPTIME = 'exptime'
    SKYDIFF = 'skydiff'
    CHISQ = 'chisq'
    NPIX = 'npix'
    AIRMASS_1 = 'airmass1'
    ANG_1 = 'ang1'
    INCLUDED = 'included'


phot_all_column_names = [ColumnName.HJD, ColumnName.FLUX, ColumnName.FLUX_ERR, ColumnName.OBS_ID,
                         ColumnName.JD, ColumnName.FWHM, ColumnName.SKY, ColumnName.AIRMASS, ColumnName.NSTAR,
                         ColumnName.SCALE, ColumnName.EXPTIME, ColumnName.SKYDIFF, ColumnName.CHISQ, ColumnName.NPIX]

phot_column_names = [ColumnName.HJD, ColumnName.FLUX, ColumnName.FLUX_ERR, ColumnName.OBS_ID,
                     ColumnName.JD, ColumnName.FWHM, ColumnName.SKY, ColumnName.AIRMASS, ColumnName.NSTAR,
                     ColumnName.SCALE, ColumnName.EXPTIME, ColumnName.SKYDIFF, ColumnName.CHISQ, ColumnName.NPIX]

phot_cor_column_names = [ColumnName.HJD, ColumnName.COR_FLUX, ColumnName.FLUX_ERR, ColumnName.OBS_ID,
                         ColumnName.JD, ColumnName.FWHM, ColumnName.SKY, ColumnName.AIRMASS, ColumnName.NSTAR,
                         ColumnName.SCALE, ColumnName.EXPTIME, ColumnName.SKYDIFF, ColumnName.CHISQ, ColumnName.NPIX,
                         ColumnName.AIRMASS_1, ColumnName.ANG_1]

merged_column_names = [ColumnName.HJD, ColumnName.FLUX, ColumnName.COR_FLUX, ColumnName.FLUX_ERR, ColumnName.OBS_ID,
                       ColumnName.JD, ColumnName.FWHM, ColumnName.SKY, ColumnName.AIRMASS, ColumnName.NSTAR,
                       ColumnName.SCALE, ColumnName.EXPTIME, ColumnName.SKYDIFF, ColumnName.CHISQ, ColumnName.NPIX,
                       ColumnName.AIRMASS_1, ColumnName.ANG_1, ColumnName.INCLUDED]

merged_column_formats = {ColumnName.HJD: '.6f',
                         ColumnName.FLUX: '.6f',
                         ColumnName.COR_FLUX: '.6f',
                         ColumnName.FLUX_ERR: '.6f',
                         ColumnName.OBS_ID: '.0f',
                         ColumnName.JD: '.6f',
                         ColumnName.FWHM: '.5f',
                         ColumnName.SKY: '.2f',
                         ColumnName.AIRMASS: '.5f',
                         ColumnName.NSTAR: '.0f',
                         ColumnName.SCALE: '.6f',
                         ColumnName.EXPTIME: '.0f',
                         ColumnName.SKYDIFF: '.4f',
                         ColumnName.CHISQ: '.6f',
                         ColumnName.NPIX: '.0f',
                         ColumnName.AIRMASS_1: '.4f',
                         ColumnName.ANG_1: '.4f'}
