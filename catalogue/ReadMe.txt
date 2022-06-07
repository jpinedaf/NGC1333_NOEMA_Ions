J/AJ/140/266     NGC 1333 X-ray luminous YSOs properties     (Winston+, 2010)
================================================================================
The properties of X-ray luminous young stellar objects in the NGC 1333 and
Serpens embedded clusters.
    Winston E., Megeath S.T., Wolk S.J., Spitzbart B., Gutermuth R.,
    Allen L.E., Hernandez J., Covey K., Muzerolle J., Hora J.L., Myers P.C.,
    Fazio G.G.
   <Astron. J., 140, 266-292 (2010)>
   =2010AJ....140..266W
================================================================================
ADC_Keywords: Associations, stellar ; X-ray sources ; Infrared sources ; YSOs
Keywords: circumstellar matter - infrared: stars - stars: pre-main sequence -
          X-rays: stars

Abstract:
    We present new Chandra X-ray data of the NGC 1333 embedded cluster and
    combine these data with existing Chandra data, Spitzer photometry, and
    ground-based spectroscopy of both the NGC 1333 and Serpens cloud core
    clusters to perform a detailed study of the X-ray properties of two of
    the nearest embedded clusters to the Sun. We first present new, deeper
    observations of NGC 1333 with Chandra ACIS-I and combine these with
    existing Spitzer observations of the region. In NGC 1333, a total of
    95 cluster members are detected in X-rays of which 54 were previously
    identified in the Spitzer data.

Description:
    We have obtained Spitzer images of the Serpens and NGC 1333 regions
    in six wavelength bands: the 3.6, 4.5, 5.8, and 8.0um bands of the
    Infrared Array Camera (IRAC) and the 24um and 70um bands of the
    Multi-band Imaging Photometer for Spitzer (MIPS). The photometry
    extracted from these data was supplemented by J-, H-, and Ks-band
    photometry from the Two Micron All Sky Survey (2MASS) point-source
    catalog.

    The X-ray data were taken from the Chandra ANCHORS (AN archive of
    Chandra Observations of Regions of Star formation11) archive. The
    Serpens cluster was observed on 2004 June 19, OBSID 4479, with an
    88.45ks exposure time.

    The NGC 1333 data are newly published here, hence we describe the
    reduction of the NGC 1333 data in detail. NGC 1333 was observed in
    three epochs: OBSID 6436, a 36.95ks exposure on 2006 July 5, OBSID
    6437, a 40.12ks exposure on 2006 July 11, and OBSID 642, a 43.91ks
    exposure on 2000 July 12, giving a total exposure time of 120.98ks.


File Summary:
--------------------------------------------------------------------------------
 FileName   Lrecl  Records  Explanations
--------------------------------------------------------------------------------
ReadMe         80        .  This file
table1.dat     82      180  NGC 1333: Chandra X-ray source photometry
table2.dat    169       95  NGC 1333: Coordinates and IR photometry of X-ray
                             sources
table3.dat     39       95  NGC 1333: IR coordinates and Chandra ID of
                             X-ray detected YSOs
table4.dat     79       64  Serpens: Spectroscopic and X-ray properties of YSOs
table5.dat     79       74  NGC 1333: Spectroscopic and X-ray properties of YSOs
--------------------------------------------------------------------------------

See also:
    J/ApJ/575/354 : Young stellar objects in the NGC 1333 (Getman+, 2002)
    J/ApJ/669/493 : Spitzer/Chandra YSOs in Serpens cloud core (Winston+, 2007)
    J/ApJ/674/336 : Spitzer observations of NGC 1333 (Gutermuth+, 2008)

Byte-by-byte Description of file: table1.dat
--------------------------------------------------------------------------------
   Bytes Format Units      Label   Explanations
--------------------------------------------------------------------------------
   1-  3  I3    ---        Seq     Sequential number <[WMW2010] NNN> in Simbad
       5  I1    h          RAh     Right ascension (J2000)
   7-  8  I2    min        RAm     Right ascension (J2000)
  10- 14  F5.2  s          RAs     Right ascension (J2000)
      16  A1    ---        DE-     Declination sign (J2000)
  17- 18  I2    deg        DEd     Declination (J2000)
  20- 21  I2    arcmin     DEm     Declination (J2000)
  23- 27  F5.2  arcsec     DEs     Declination (J2000)
  29- 32  I4    ct         RawCt   Raw counts
  34- 40  F7.2  ct         NCt     Net Counts, background subtracted and
                                    aperture corrected from raw counts
  42- 47  F6.2 10+22cm-2   NH     ? Hydrogen column density
  49- 52  F4.2 10+22cm-2 e_NH     ? rms uncertainty on NH
  54- 58  F5.2  keV        kT     ? Plasma temperature
  60- 63  F4.2  keV      e_kT     ? rms uncertainty on kT
  65- 70  F6.2  [mW/m2]    FluxA  ? Absorbed X-ray flux
  72- 77  F6.2  [mW/m2]    FluxU  ? Total unabsorbed X-ray flux
  79- 82  F4.2  ---        chi2   ? chi^2^ value
--------------------------------------------------------------------------------

Byte-by-byte Description of file: table2.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label     Explanations
--------------------------------------------------------------------------------
   1-  3  I3    ---     Seq       Sequential number <[WMW2010] NNN> in Simbad
       5  I1    h       RAh       X-ray Riht ascension (J2000)
   7-  8  I2    min     RAm       X-ray Right ascension (J2000)
  10- 14  F5.2  s       RAs       X-ray Right ascension (J2000)
      16  A1    ---     DE-       X-ray Declination sign (J2000)
  17- 18  I2    deg     DEd       X-ray Declination (J2000)
  20- 21  I2    arcmin  DEm       X-ray Declination (J2000)
  23- 27  F5.2  arcsec  DEs       X-ray Declination (J2000)
      29  I1    h       RAIh      Infrared Right ascension (J2000) (1)
  31- 32  I2    min     RAIm      Infrared Right ascension (J2000) (1)
  34- 38  F5.2  s       RAIs      Infrared Right ascension (J2000) (1)
      40  A1    ---     DEI-      Infrared Declination sign (J2000) (1)
  41- 42  I2    deg     DEId      Infrared Declination (J2000) (1)
  44- 45  I2    arcmin  DEIm      Infrared Declination (J2000) (1)
  47- 52  F6.3  arcsec  DEIs      Infrared Declination (J2000) (1)
  54- 58  F5.3  arcsec  Sep       Separation (2)
      60  A1    ---   l_Jmag      Limit flag on Jmag
  61- 66  F6.3  mag     Jmag      ?=- 2MASS J magnitude
  68- 72  F5.3  mag   e_Jmag      ? rms uncertainty on Jmag
      74  A1    ---   l_Hmag      Limit flag on Hmag
  75- 80  F6.3  mag     Hmag      ?=- 2MASS H magnitude
  82- 86  F5.3  mag   e_Hmag      ? rms uncertainty on Hmag
  88- 93  F6.3  mag     Kmag      ?=- 2MASS Ks magnitude
  95- 99  F5.3  mag   e_Kmag      ? rms uncertainty on Kmag
 101-107  F7.4  mag     [3.6]     ?=- Spitzer/IRAC 3.6um magnitude
 109-113  F5.3  mag   e_[3.6]     ? rms uncertainty on [3.6]
 115-121  F7.4  mag     [4.5]     ?=- Spitzer/IRAC 4.5um magnitude
 123-127  F5.3  mag   e_[4.5]     ? rms uncertainty on [4.5]
 129-135  F7.4  mag     [5.8]     ?=- Spitzer/IRAC 5.8um magnitude
 137-141  F5.3  mag   e_[5.8]     ? rms uncertainty on [5.8]
 143-149  F7.4  mag     [8.0]     ?=- Spitzer/IRAC 8.0um magnitude
 151-155  F5.3  mag   e_[8.0]     ? rms uncertainty on [8.0]
 157-163  F7.4  mag     [24]      ?=- Spitzer/MIPS 24um magnitude
 165-169  F5.3  mag   e_[24]      ? rms uncertainty on [24]
--------------------------------------------------------------------------------
Note (1): The IR detections in multiple bands are matched to <1", with the
           coordinates at the shortest detected wavelength listed
Note (2): Three sources match to IR detections with separations >1":
           12, 135, 188.
--------------------------------------------------------------------------------

Byte-by-byte Description of file: table3.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label    Explanations
--------------------------------------------------------------------------------
   1-  3  I3    ---     SID      Spitzer identifier from Gutermuth et al. (2008,
                                 Cat. J/ApJ/674/336) <[GMM2008] NNN> in Simbad
       5  I1    h       RAh      Right ascension (J2000)
   7-  8  I2    min     RAm      Right ascension (J2000)
  10- 14  F5.2  s       RAs      Right ascension (J2000)
      16  A1    ---     DE-      Declination sign (J2000)
  17- 18  I2    deg     DEd      Declination (J2000)
  20- 21  I2    arcmin  DEm      Declination (J2000)
  23- 27  F5.2  arcsec  DEs      Declination (J2000)
  29- 31  A3    ---     Class    Classification (1)
  33- 35  I3    ---     Seq      Sequential number <[WMW2010] NNN> in Simbad
  37- 39  I3    ---     GID      ? Getman et al. (2002, Cat. J/ApJ/575/354)
                                   identifier, [GFT2002] NNN in Simbad
--------------------------------------------------------------------------------
Note (1): Evolutionary classification modified from that of Gutermuth et al.
   (2008, Cat. J/ApJ/674/336) based on Winston et al. (2007, Cat. J/ApJ/669/493)
   as follows:
      I = Class I
     FS = flat spectrum
     II = Class II
     TD = transition disk
    III = Class III
--------------------------------------------------------------------------------

Byte-by-byte Description of file: table4.dat
--------------------------------------------------------------------------------
  Bytes Format Units    Label   Explanations
--------------------------------------------------------------------------------
  1-  3  I3    ---      SID     Spitzer identifier, from Winston et al.,
                                 2009AJ....137.4777W,
                                 [WMW2007] NNN, in Simbad (G1)
  5-  8  A4    ---      SpT     MK spectral type
 10- 12  F3.1  ---    e_SpT     ? Uncertainty on SpT
 14- 18  A5    ---      Class   YSO Classification (G2)
 20- 22  I3    ---      Seq     ? Chandra sequential number
 24- 29  F6.3  [Lsun]   logLbol Bolometric magnitude
 31- 36  F6.1  K        Teff    Effective temperature
 38- 45  F8.3  [Sun]    logSA   Stellar surface area, in solar units
 47- 51  F5.2  [10-7W]  logLX   ? X-ray luminosity
 53- 57  F5.2  keV      kT      ? Plasma temperature
 59- 63  F5.3 10+22cm-2 NH      ? Hydrogen column density
 65- 68  F4.2  mag      AK      ? Absorption in K band (G3)
     70  A1    ---    l_Age     [~] Limit flag on Age
 71- 74  F4.1  Myr      Age     ? Isochronal age (G4)
 76- 79  F4.2  Msun     Mass    ? Isochronal mass (G4)
--------------------------------------------------------------------------------

Byte-by-byte Description of file: table5.dat
--------------------------------------------------------------------------------
  Bytes Format Units    Label   Explanations
--------------------------------------------------------------------------------
  1-  3  I3    ---      SID     Spitzer identifier, Gutermuth et al.
                                 (2008, Cat. J/ApJ/674/336),
                                 <[GMM2008] NNN> in Simbad (G1)
  5-  8  A4    ---      SpT     MK spectral type
 10- 12  F3.1  ---    e_SpT     ? Uncertainty on SpT
 14- 18  A5    ---      Class   YSO Classification (G2)
 20- 22  I3    ---      Seq     ? Sequential number, <[WMW2010] NNN> in Simbad
 24- 29  F6.3  [Lsun]   logLbol Bolometric magnitude
 31- 36  F6.1  K        Teff    Effective temperature
 38- 45  F8.3  [Sun]    logSA   Stellar surface area, in solar units
 47- 51  F5.2  [10-7W]  logLX   ? X-ray luminosity
 53- 57  F5.2  keV      kT      ? Plasma temperature
 59- 63  F5.3 10+22cm-2 NH      ? Hydrogen column density
 65- 68  F4.2  mag      AK      ? Absorption in K band (G3)
     70  A1    ---    l_Age     [~] Limit flag on Age
 71- 74  F4.1  Myr      Age     ? Isochronal age (G4)
 76- 79  F4.2  Msun     Mass    ? Isochronal mass (G4)
--------------------------------------------------------------------------------

Global notes:
Note (G1): See Tables 6 and 4 of Winston et al. (2009AJ....137.4777W) for
   coordinates and magnitudes associated with spectra.
Note (G2): Classification as follows:
    0/I =  Class 0/I
     FS =  flat spectrum
     II =  Class II
     TD =  transition disk
    III =  X-ray detected Class III
  [III] = new candidate Class IIIs with detected Li i absorption
Note (G3): A value of zero indicates that the source was blueward of the CTTS
    locus, and a null value indicates that a value could not be calculated.
Note (G4): Isochronal age and mass are determined by interpolation from the
     Baraffe (1998, Cat. J/A+A/337/403) tracks. Age of ~0.2 indicates that
     the source is very young but on the edge of isochrone grid.
--------------------------------------------------------------------------------

History:
    From electronic version of the journal

================================================================================
(End)                                      Patricia Vannier [CDS]    09-Jun-2012
