This folder contains two files about US NRC radwaste classification.
See NRC website and '10CFR61' for more information.
- USNRC_LL.csv: Long live nuclides table.
- USNRC_SL.csv: Short live nuclides table.

Data in USNRC_LL.csv have two units:
- Ci/g: for Pu241 and Cm242
- Ci/m3: for the rest
- There is not class B in orignal USNRC_LL, to keep the format of table LL
  and SL are the same, I set the limit of class A and B to be the same.
  Therefore, if the radwaste exceed the class A, it automatically exceed the
  limit of calss B.
  

Data in USNRC_SL.csv ara in unit of: Ci/m3.
- The nuclide with half life less than 5 year, is hard coded, not present in the csv.

DATA in USNRC_EDE_MASS.csv are the mass-based normalized effective dose
equivalents to critical groups for all materials, in unit of: uSv/yr per Bq/g.
Table 2.1 in Ref[1].
The the clearance limit is expressed in Becquerels per gram and can be derived
by dividing the recommended 10 mSv/yr dose standard by the mass-based
effective dose equivalent in microSieverts per year per Becquerels per
gram, for the individual radionuclide. Ref[2]
Reference:
- [1] Anigstein, Robert, Harry Chmelynski, Donald Loomis, Stephen Marschket, John Mauro, Richard Olsher, William Thurber, and Robert Meck. “Radiological Assessments for Clearance of Materials from Nuclear Facilities (NUREG-1640).” Washington  D.C.: U.S.  Nuclear  Regulatory  Commission, June 2003. https://www.nrc.gov/reading-rm/doc-collections/nuregs/staff/sr1640/index.html.
- [2] El-Guebaly, L., P. Wilson, D. Paige, Aries Team, and Z-Pinch Team. “Evolution of Clearance Standards and Implications for Radwaste Management of Fusion Power Plants.” Fusion Science and Technology 49, no. 1 (January 2006): 62–73. https://doi.org/10.13182/FST06-2.


