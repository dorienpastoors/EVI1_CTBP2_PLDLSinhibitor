# EVI1_CTBP2_PLDLSinhibitor

This is all custom R and python code used in our manuscript:
"Oncogene EVI1 Drives Acute Myeloid Leukemia Via a Targetable Interaction with CTBP2"

## AlphaFold

* Data for script (the predicted structures, as well as the ChimeraX output) is available on Zenodo INSERT DOI
* chimerax_quantification.RMD is the R script required to generate the input for the AlphaFold heatmaps
* python_cmds_chimerax_*.py are python scripts for quantification of interaction. Running these scripts *within* ChimeraX will generate interaction tables like the ones available for this project. 

## ChIP-seq correlation plots
* data for script is normally generated from BAM files
* for the purpose of recreating the plots a count matrix of associated files is also uploaded

## Data availability
* open data is available on Zenodo
* this includes all tables for flow cytometry, luciferase measurements (in vivo and for MAPPIT assay) and mass-spec results
* all predicted alphafold structures are available on Zenodo

## Data availability per figure panel

| figure panel          | data type                      | location                                                                    | accession                                                                                    | name_supplementary_data                                                               | data format                              |
| --------------------- | ------------------------------ | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ---------------------------------------- |
| 1A                    | mass_spectrometry              | ProteomeXChange                                                             | PXD043333                                                                                    | MassSpec_MUTZ3_EVI1vsIgG.txt                                                          | text                                     |
| 1A                    | mass_spectrometry              | ZENODO                                                                      | 10.5281/zenodo.8354861                                                                       | MassSpec_MUTZ3_EVI1vsIgG.txt                                                          | text                                     |
| 1B & S1B              | mass_spectrometry              | ZENODO                                                                      | 10.5281/zenodo.8354861                                                                       | MassSpec_MUTZ3_EVI1vsIgG_Clusters.txt                                                 | text                                     |
| S1D                   | mass_spectrometry              | ZENODO                                                                      | 10.5281/zenodo.8354861                                                                       | MassSpec_NFS78_BiotagvsNoBiotag.txt; MassSpec_NFS78_BiotagvsNoBiotag_designTable.xlsx | text & xlsx                              |
|                       |                                |                                                                             |                                                                                              |                                                                                       |                                          |
| 1C, 1E, S2B, 3D, 3F   | chip_seq                       | GEO                                                                         | GSE236010                                                                                    | Raw FASTQ files, peakfiles and BIGWIG                                                 | various                                  |
| chip_seq              | github                         | [Github & Geo](https://github.com/dorienpastoors/EVI1_CTBP2_PLDLSinhibitor) | chipseq-corrplots/CTBP_Mutz3_peaks.narrowPeak; chipseq-corrplots/EVI1_Mutz3_peaks.narrowPeak | narrowPeak                                                                            |
| 3F                    | chip_seq                       | ZENODO                                                                      | 10.5281/zenodo.8354861                                                                       | ChIPseq_EVI1_2747.bigwig                                                              | bigwig                                   |
| 1D, S2A               | chip_seq                       | github                                                                      | [Github](https://github.com/dorienpastoors/EVI1_CTBP2_PLDLSinhibitor)                        | chipseq-corrplots/counts_CTBP2peaks.txt;chipseq-corrplots/counts_EVI1peaks.txt        | text                                     |
| chip_seq              | github                         | [Github](https://github.com/dorienpastoors/EVI1_CTBP2_PLDLSinhibitor)       | chipseq-corrplots/heatmaps_corr.RMD                                                          | .RMD                                                                                  |
| S4A, S4B              | chip_seq                       | ZENODO                                                                      | 10.5281/zenodo.8354861                                                                       | DiffBind_20230816_PLASSvsPLDLS_CTBP2.csv                                              | csv                                      |
| S4D                   | chip_seq                       | ZENODO                                                                      | 10.5281/zenodo.8354861                                                                       | CTBP2UntreatedTrackannot_PeaksToGenes.txt                                             | tsv                                      |
|                       |                                |                                                                             |                                                                                              |                                                                                       |                                          |
| S4C                   | rna_seq                        | GEO                                                                         | GSE236010                                                                                    | Raw FASTQ files and quant.sf                                                          | various                                  |
| rna_seq               | ZENODO                         | 10.5281/zenodo.8354861                                                      | deseq2_apeGLMLog2FC_PLDLSvsPLASS.txt                                                         | text                                                                                  |
|                       |                                |                                                                             |                                                                                              |                                                                                       |                                          |
| 2A, 3A                | alphafold_predicted_structures | ZENODO                                                                      | 10.5281/zenodo.8354861                                                                       | AlphaFold_Predictions.zip                                                             | zipped_folder [pdb, txt and fasta files] |
| 2B                    | chimerax_python_scripts        | github                                                                      | [Github](https://github.com/dorienpastoors/EVI1_CTBP2_PLDLSinhibitor)                        | alphafold_quantResidues/AlphaFold_python_cmds_chimerax_\*.py                          | .py script                               |
| chimerax_r_scripts    | github                         | [Github](https://github.com/dorienpastoors/EVI1_CTBP2_PLDLSinhibitor)       | alphafold_quantResidues/alphafold_quant_int_res_gitversion.rmd                               | .RMD                                                                                  |
| chimerax_contacts     | github                         | [Github](https://github.com/dorienpastoors/EVI1_CTBP2_PLDLSinhibitor)       | alphafold_quantResidues/chimerax_contacts_\*.txt                                             | text                                                                                  |
|                       |                                |                                                                             |                                                                                              |                                                                                       |                                          |
| 4C, 5E                | flow_cytometry                 | ZENODO                                                                      | 10.5281/zenodo.8354861                                                                       | FlowCytometry_Gating.pdf                                                              | PDF                                      |
| 5F, 5H                | flow_cytometry                 | ZENODO                                                                      | 10.5281/zenodo.8354861                                                                       | FlowCytometry_SB1690_MixExperiments_FrequencyTables.xlsx                              | xlsx                                     |
|                       |                                |                                                                             |                                                                                              |                                                                                       |                                          |
| 5C                    | luciferase_outgrowth           | ZENODO                                                                      | 10.5281/zenodo.8354861                                                                       | LuciferaseSize_MUTZ3_ScaffoldMice.xlsx                                                | .xlsx                                    |
| S2C, 2C, 3C, S3A      | western_blot                   | ZENODO                                                                      | 10.5281/zenodo.8354861                                                                       | full uncropped western blots                                                          | PDF                                      |
| 2D, 2E,  S3B, S3C, 3B | mappit_data                    | ZENODO                                                                      | 10.5281/zenodo.8354861                                                                       | mappit.zip                                                                            | zipped folder [.pfzx & .xlsx]            |
| 2F, 4B, 5A            | colony_assay                   | ZENODO                                                                      | 10.5281/zenodo.8354861                                                                       | colony_assays.zip                                                                     | zipped folder [.pfzx & .csv]             |
Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
