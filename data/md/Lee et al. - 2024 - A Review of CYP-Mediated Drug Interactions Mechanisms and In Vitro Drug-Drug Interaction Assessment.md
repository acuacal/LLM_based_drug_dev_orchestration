<!-- image -->

<!-- image -->

Review

## AReview of CYP-Mediated Drug Interactions: Mechanisms and In Vitro Drug-Drug Interaction Assessment

<!-- image -->

Jonghwa Lee *, Jessica L. Beers, Raeanne M. Geffert and Klarissa D. Jackson *

<!-- image -->

Division of Pharmacotherapy and Experimental Therapeutics, UNC Eshelman School of Pharmacy, University of

North Carolina at Chapel Hill, Chapel Hill, NC 27599, USA; jlbeers@uw.edu (J.L.B.); geffert@unc.edu (R.M.G.)

- * Correspondence: jlee497@email.unc.edu (J.L.); klarissa.jackson@unc.edu (K.D.J.)

Abstract: Drug metabolism is a major determinant of drug concentrations in the body. Drug-drug interactions (DDIs) caused by the co-administration of multiple drugs can lead to alteration in the exposure of the victim drug, raising safety or effectiveness concerns. Assessment of the DDI potential starts with in vitro experiments to determine kinetic parameters and identify risks associated with the use of comedication that can inform future clinical studies. The diverse range of experimental models and techniques has significantly contributed to the examination of potential DDIs. Cytochrome P450 (CYP) enzymes are responsible for the biotransformation of many drugs on the market, making them frequently implicated in drug metabolism and DDIs. Consequently, there has been a growing focus on the assessment of DDI risk for CYPs. This review article provides mechanistic insights underlying CYP inhibition/induction and an overview of the in vitro assessment of CYP-mediated DDIs.

Keywords: cytochrome P450; drug metabolism; drug-drug interaction; inhibition; induction; reaction phenotyping

## 1. Introduction

In clinical practice, the increasing prevalence of multiple drug therapy presents an ongoing challenge, with drug interactions being a significant concern [1]. These interactions, known as drug-drug interactions (DDIs), often result from the changes in a victim drug's plasma concentrations due to a perpetrator drug either inhibiting or inducing the metabolism or transport of the victim drug [1,2]. Consequently, DDIs may lead to changes in the pharmacokinetic (PK) profile with reduced efficacy and/or unexpected toxicities. Enzyme- or transporter-mediated inhibition of drug elimination can lead to increased area under the curve (AUC), maximum plasma concentration (Cmax), and half-life (t 1/2 ) [3]. Conversely, induction generally leads to reduced AUC, Cmax, and t 1/2 . Several drugs, such as terfenadine, mibefradil, cisapride, and nefazodone, have been removed from the market due to adverse reactions mediated by DDIs, necessitating assessment of DDI potential during drug development and post-marketing approval [1,4]. Assessment of the potential for DDI of a drug comprises three steps [5]. First, it requires the identification of the primary pathways through which the drug is eliminated from the body. Second, it involves estimating the contribution of drug-metabolizing enzymes and transporters to the disposition in the body. Lastly, it entails characterizing how the drug influences the function of drug-metabolizing enzymes and transporters.

Many therapeutic drugs undergo hepatic metabolism. Thus, when evaluating DDIs, PK interaction studies focus on the association of the test drug with drug-metabolizing enzymes [2,6]. Cytochrome P450 (CYP) enzymes are a superfamily of enzymes primarily found in the liver, but also in other tissues including the intestines, kidneys, lungs, and brain. CYPs are capable of catalyzing oxidative biotransformation of 70-80% of drugs in the market [7]. Among the 57 putatively functional human CYPs, CYP1A2, CYP2B6, CYP2C8, CYP2C9, CYP2C19, CYP2D6, and CYP3A4/5 are the predominant forms expressed in the

<!-- image -->

Citation: Lee, J.; Beers, J.L.; Geffert, R.M.; Jackson, K.D. A Review of CYP-Mediated Drug Interactions: Mechanisms and In Vitro Drug-Drug Interaction Assessment. Biomolecules 2024 , 14 , 99. https://doi.org/ 10.3390/biom14010099

Academic Editor: Nuno Vale

Received: 15 December 2023

Revised: 2 January 2024

Accepted: 8 January 2024

Published: 12 January 2024

<!-- image -->

Copyright: © 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ 4.0/).

liver, and they are frequently implicated in drug metabolism and DDIs [2,7]. Regulatory agencies frequently update their guidelines on DDI studies, with particular focus on CYP enzymes, due to safety concerns associated with these interactions. The guidelines provide considerations when choosing experimental conditions such as test system, probe substrates, and positive controls [2].

The United States Food and Drug Administration (FDA) recently issued a new guideline standard entitled 'In vitro Drug Interaction Studies-Cytochrome P450 Enzyme- and Transporter-Mediated Drug Interactions' in 2020. Results from in vitro experiments can be translated for in vivo predictions or the design of clinical studies by using various modeling methods [2,5]. Examples of commonly used in vitro marker reactions, inhibitors, and inducers for CYP-mediated drug metabolism are shown in Table 1. This article reviews the current understanding of mechanisms of CYP inhibition/induction and in vitro approaches to assess CYP-mediated DDIs. It is important to acknowledge that while CYPs are often associated with drug-metabolizing enzymes and may be the main route of elimination for many drugs, transporters also contribute to the appearance of DDIs and should also be characterized according to the FDA guidance [5,8]. However, transporter-mediated DDIs are not in the scope of this review.

Table 1. Examples of in vitro substrate marker reactions, inhibitors, and inducers for CYP-mediated drug metabolism.

| CYP Enzyme                                                                                                       | Substrate Marker Reactions                                                                                          | Inhibitors               | Inducers   |
|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|--------------------------|------------|
| Caffeine 3- N -demethylation [9-11] 7-ethoxyresorufin O -deethylation [12-14] Phenacetin O -deethylation [15-18] | Amiodarone [19,20] Cimetidine [22-24] Furafylline [15,18,25,26] α -Naphthoflavone [27,28]                           | Omeprazole [15,21]       | 1A2        |
| Bupropion hydroxylation [17,18,29] Efavirenz hydroxylation [30]                                                  | Clopidogrel [31,32] Ticlopidine [31,32] Sertraline [32,37] Thiotepa [31,38] 2-phenyl-2-(1-piperidyl)propane [32,39] | Phenobarbital [33-36]    | 2B6        |
| Amodiaquine N -deethylation [18,40,41] Paclitaxel 6 α -hydroxylation [40,42]                                     | Gemfibrozil [43] Montelukast [45] Phenelzine [46]                                                                   | Rifampicin [34,36,44]    | 2C8        |
| Diclofenac 4 ' -hydroxylation [18,47-49] S -warfarin 7-hydroxylation [48]                                        | Sulfaphenazole [18,49-51] Tienilic acid [17,53]                                                                     | Rifampicin [34,36,44,52] | 2C9        |
| S -mephenytoin 4 ' -hydroxylation [54]                                                                           | N -3-benzylnirvanol [55] Ticlopidine [51,56] Loratadine [57] Nootkatone [58]                                        | Rifampicin [36]          | 2C19       |
| Bufuralol 1 ' -hydroxylation [49,59] Dextromethorpan O -demethylation [18,62]                                    | Quinidine [18,49,60,61] Paroxetine [61,63]                                                                          |                          | 2D6        |
| Midazolam 1 ' -hydroxylation [17,49,64-66] Testosterone 6 β -hydroxylation [17]                                  | Ketoconazole [17,49,50,64-66] CYP3Cide (3A4 specific) [65,66]                                                       | Rifampicin [15,34,36,67] | 3A4/5      |

## 2. Reaction Phenotyping

## 2.1. Overview of Reaction Phenotyping

It is critical to determine if a drug candidate is a substrate for a CYP enzyme prior to administration to a patient. This is to ensure the drug does not have DDIs that may be of clinical significance. Additionally, knowledge of major metabolizing enzymes can help with any pharmacogenetic, disease state, or environmental considerations [68]. Reaction phenotyping is a commonly used in vitro approach to identify the enzymes and pathways responsible for metabolizing a drug [69-72]. This is an important step to assess the potential for DDIs as some metabolic pathways may compete for the same enzymes. This type of

characterization is recommended for industry sponsors according to the FDA guidance [5]. Understanding the in vitro contributions of CYP enzymes to the overall metabolism of a drug is one of the first steps to determining the need for clinical DDI studies. The main goals of reaction phenotyping are to (1) determine the fraction metabolized by each CYP involved in the metabolic clearance, (2) characterize enzyme kinetics and other in vitro parameters, and (3) provide an early screen for potential DDIs [68,69,73-75].

## 2.1.1. Fraction Metabolized (fm)

The fraction metabolized (fm) refers to the extent a substrate undergoes hepatic metabolism by a specific enzyme. The fm value is specific to an individual enzyme and substrate. A high fm value (fm > 0.9) means one enzyme is primarily responsible for the majority of the metabolism of a substrate. This is considered a DDI concern especially if the main route of elimination for the compound is metabolism. In general, the pharmaceutical industry seeks to reduce the fm value of a compound by introducing structural modifications to reduce the risk for the drug candidate being a victim of DDIs [74]. The fm can be determined by multiple reaction phenotyping approaches, which are explained in the following sections. The fm value is described by:

f m = CL int,sc,u CYPx CL int,sc,u CYP total

where CL int,sc,u CYPx represents the intersystem extrapolation factor (ISEF) scaled value from a single CYP enzyme, and the CL int,sc,u CYP total term is the sum of all scaled values in the system.

## 2.1.2. In Vitro Pharmacokinetic Parameters

Examining in vitro PK parameters is crucial for understanding in vivo effects [2,76]. At steady state, the concentration of the enzyme-substrate complex, treated as a reactive intermediate, remains constant, and any fluctuations in substrate concentration are insignificant [76]. This assumption underlies efforts to maintain minimal substrate turnover (<10%) in experiments aimed at determining enzyme kinetic parameters. It also implies a necessity for the substrate concentration to significantly exceed the enzyme concentration. Therefore, alterations in substrate concentration resulting from enzyme-substrate complex formation are deemed negligible, necessitating the maintenance of the lowest possible enzyme concentration to meet this criterion [76]. These parameters include the Vmax, or the maximal velocity (or rate) that an enzyme can catalyze a reaction when it is fully saturated with substrate; Km, the substrate concentration at half-maximal enzyme velocity; the CL int , the intrinsic clearance or efficiency that a process can eliminate a drug, specifically through metabolism; t 1/2 , or half-life, the time it takes for half of the drug to be eliminated; and f CL , or the fraction of metabolic clearance proceeding through a pathway [11]. The CL int ,u is calculated as follows:

CL int,u = ( Vmax / Km × CYP abundance per mg of HLM ) F u,mic × ISEF ( CL int )

where CL int,u is the intrinsic unbound clearance, Vmax is the maximal velocity, Km is the Michaelis-Menten constant, F u,mic is the fraction unbound in microsomes, HLM is human liver microsomes, and ISEF is the intersystem extrapolation factor (see below) [77]. It is important to determine the unbound value for clearance as the unbound drug is responsible for pharmacological activity in the system, and is able to cross membranes, whereas the bound drug is not. However, this is often difficult to determine as total drug concentration is typically sampled in these systems. For highly bound drugs, the FDA guidance states that the unbound fraction in plasma should be considered 1% (fu,p = 0.01), if experimentally determined to be less than one percent. Additionally, the CL int may be determined through

substrate depletion experiments. These experiments may be completed with microsomes or hepatocytes in order to estimate in vitro intrinsic clearance [78].

## 2.1.3. Drug-Drug Interaction Implications

When considering PK DDIs, the equation by Rowland and Matin is often used [79]:

Ratio = 1 fm 1 + ( [ I ] K I ) +( 1 -fm )

where fm is the fraction metabolized, [I] is the inhibitor concentration, and K I is the inhibition constant. For DDI predictions, the ratio is the AUC in the presence and absence of inhibitor (AUCR). Based on this equation, when fm increases, the potential for a DDI also increases [79]. This shows the relationship between fm value and DDI risk, and therefore highlights the importance of determining the fm value. The FDA guidance recommends in vivo clinical studies when ≥ 25% of the clearance is from one enzyme [5]. However, definitive information for the major drug clearance pathways can only be determined from an in vivo radiolabeled study [74].

## 2.2. Reaction Phenotyping Approaches

There are three main approaches to reaction phenotyping: (1) selective inhibition with chemical inhibitors or antibodies, (2) an individually cDNA expressed recombinant CYP (rCYP) panel, and (3) correlation analyses to CYP activities determined in individual human liver microsome (HLM) donors [69]. These approaches may be used individually, but are often combined, and results are compared for accuracy and agreement [80,81].

## 2.2.1. Chemical Inhibition Approach

The chemical inhibition approach refers to using chemical inhibitors with well-defined and specific selectivity in a human-derived in vitro hepatic system [75]. This is often performed with a single concentration of a well-studied inhibitor [2,68,75]. It is critical that the inhibitor has defined selectivity toward a specific target enzyme. Recommended chemical inhibitors are described by the FDA in vitro selective inhibitors for CYP-mediated metabolism and are included in Table 1 [82]. The potency and selectivity of inhibitors should be assessed prior to use in a reaction phenotyping study [2,68,75]. Inhibitory antibodies can also be used for this approach [83,84]. However, these antibodies do not always reach maximal inhibition [84].

## 2.2.2. Recombinant CYP Panel (RAF/ISEF Method) Approach

In this method for reaction phenotyping, a panel of rCYP enzymes with known activity and normalized for protein are incubated with the drug of interest, and a scaling factor is applied to the final parameters to account for the full liver rather than only the individual enzymes [73,85]. The panel typically includes CYP1A2, 2B6, 2C8, 2C9, 2C19, 2D6, and 3A4 and 3A5 [5,80]. Once the in vitro kinetic parameters are scaled, the CL int is estimated [81]. Either the ISEF or the relative activity factor (RAF) may be used. The ISEF scaling factor is calculated as follows:

CLint ISEF = Vmax /Km ( HLM ) Vmax /Km ( rCYP ) × CYP abundance ( HLM )

where CYP abundance (HLM) is represented as the picomoles of CYP per milligram of protein [73,85]. It is important to note that scaling factors can be affected by which probe substrate is used to derive them.

The RAF is calculated as follows [86]:

RAF = Vmax,HLM /Km,u,HLM Vmax,rCYP /Km,u,rCYP

where Km,u is the Km corrected for unbound fraction. These equations are used to scale the in vitro clearance values from the recombinant CYP enzyme to HLMs.

## 2.2.3. Correlation Analysis Approach

The correlation analysis approach uses the relationship between the rate of a metabolite formed and the marker activity of a specific CYP in a panel of HLMs from multiple donors [2]. A major limitation of the correlation analysis is that it does not provide fm values and is generally only used when the contribution by a single enzyme is significant [80].

## 2.2.4. Qualitative-then-Quantitative Approach

A new methodology has recently been developed that sequentially combines the use of an rCYP panel followed by use of varying concentrations of selective chemical inhibitors in pooled HLM [75]. In this qualitative-then-quantitative approach, an rCYP screening panel is employed to qualitatively show which CYP enzymes have the ability to metabolize the parent drug to metabolites of interest. Following the qualitative screen, the drug is incubated in HLM with increasing concentrations of selective inhibitors for the CYP enzymes identified in the first step to quantify the extent of inhibition. Departing from using one or two of the previously described methodologies and comparing for agreement, this new approach adopts a pre-defined selection of CYPs that have been shown to metabolize the drug. The subsequent detailing approach with selective inhibitors is used to determine the fraction of metabolic clearance through a particular pathway (f CL ) and ultimately, the fm. This approach yields more accurate estimations of fm not overestimating contributions of CYP enzymes to the overall metabolism. Additionally, it addresses the issue that using two different methods of reaction phenotyping often results in fm values that do not agree.

The qualitative-then-quantitative methodology has been applied in the literature and has revealed the metabolism of the antibiotic drug linezolid to be more complex and implicated additional CYP enzymes than previously reported [75,87]. The expanded rCYP screening by Wyndalda et al. included the most commonly implicated CYP enzymes (CYP1A2, 2C8, 2C9, 2C19, 2D6, 3A4, and 3A5) and less commonly identified CYPs in drug metabolism (CYP1A1, 2A6, 2B6, 2E1, and 4A11) [88]. In a recent study, the use of additional rCYPs showed that CYP2J2, 4F2, and 1B1 metabolize linezolid, which was not previously shown in the literature [87]. The specific contributions of each CYP were then determined with specific inhibitors of each CYP involved in metabolism. This application of the qualitative-then-quantitative approach shows how important enzymatic contributions may be overlooked by using only the chemical inhibition approach or a less-extensive rCYP panel [75,87].

## 2.2.5. Additional Methodologies

There are additional methods that may be used in conjunction with the approaches defined previously. Radioactive ([ 14 C]-labeled) compounds are often used and usually preferred to non-labeled compounds in in vitro systems. The assessment and calculation of fm and RAF/ISEF scaling factors are most accurately accomplished with the use of a radiolabeled compound, which is typically available during pre-clinical development [81]. If non-radiolabeled compounds are used, the results should be followed up with a bioanalytical study [80].

Machine learning algorithms are being investigated to better predict in vitro to in vivo extrapolations (IVIVE) from in vitro work. It is challenging to determine in vivo clearance and fm and new models may help to bridge the gap. Recent work has used only the structure of the compound to predict the contribution ratio of a specific enzyme involved in metabolism [89]. This work has shown that in vivo values can be predicted in this way and are similar to in vitro values obtained in the lab [89]. Other work in this space includes creating machine learning models to extrapolate in vivo parameters from in vitro inputs. Another study compared various machine learning models, which predicted in vivo

human intravenous (IV) clearance from in vitro data, and showed that the machine learning models were able to predict the in vivo clearance values for 16 Pfizer compounds from their respective clinical studies [90]. This model used inputs from over 600 molecules and used chemical structures, ionization, and logP, and in vitro experimental parameters including CL int , cell density, and fu, in order to predict in vivo IV clearance. SIMCYP ® software (Certara, Sheffield, UK) has also been employed to calculate the fraction and rate of metabolism of compounds based on in vitro data. The in vitro data was then used to predict DDI issues with ketoconazole, which may be concomitantly administered [91]. Modeling frameworks based on in vitro data can help to guide researchers on how and when to proceed with clinical DDI studies and provide substantial information on disposition before first-in-human (FIH) trials.

## 2.3. Limitations of Reaction Phenotyping

Although reaction phenotyping is relatively quick, robust, and reproducible in validated systems, there are limitations of the commonly used systems that must be considered. Amain concern of using the selective inhibitor approach is the lack of specificity of some inhibitors [58,92,93]. A proposed strategy to overcome this limitation is a six-parameter inhibition curve fitting approach [68]. This method can generate more accurate values for estimates of enzyme contributions by compensating for overlapping effects of inhibition profiles [73].

Another limitation is that of the HLM system. This system only maintains activity for about 1-2 h once thawed [94]. Hepatocytes in suspension can also be a viable option but only have a 4-6 h incubation period [95,96]. This provides a challenge for low turnover compounds, which may have a significantly longer half-life in vitro. Some work has been completed to provide other options for these compounds. The HepatoPac ® co-culture model has been used as a new model for low-turnover compounds [97,98]. The turnover of slowly metabolized compounds alprazolam and tolbutamide was two-fold greater in the HepatoPac ® model as compared to only suspended hepatocytes [97]. In a separate study, fm values for 10 out of 13 CYP3A4 substrates were determined to be within two-fold of the in vivo value [98]. Validated alternative systems can be a good way to overcome the limitations of the HLM system.

These alternative systems can also help to overcome another limitation of the HLM system. The microsomal system is a fraction of the liver that contains enzymes localized in the endoplasmic reticulum membrane, including CYPs, flavin-containing monooxygenase (FMO), and UDP-glucuronyltrasferases (UGTs) [99,100]. This excludes cytosolic enzymes, including aldehyde oxidase (AO), monoamine oxidase (MAO), xanthine oxidase (XO), and alcohol/aldehyde dehydrogenase (ADH/ALDH) [5]. Carboxylesterases (CES) are localized in both the microsomal and cytosolic fractions. Although it is rare for a cytosolic enzyme to be the primary metabolizing enzyme for a drug, using a microsomal system alone may hide the contributions of cytosolic enzymes [101].

## 3. CYP Inhibition

## 3.1. Mechanisms of CYP Inhibition

Assessment of a drug's potential to inhibit CYP enzymes is a multifaceted process that begins early in the preclinical phase of drug development. CYP enzymes typically contain both active and allosteric sites for binding multiple ligands, which may act as substrates, inhibitors, and/or activators. CYP inhibition may be broadly divided into reversible, quasi-irreversible, and irreversible inhibition.

## 3.1.1. Reversible Inhibition

There are four types of reversible inhibition: competitive, non-competitive, uncompetitive, and mixed competitive/non-competitive inhibition [102]. For all types of reversible inhibition, enzyme function is restored after dissociation of the inhibitor from the active or allosteric site. The duration of reversible inhibition in vivo therefore depends on the

Biomolecules

2024

,

14

, x FOR PEER REVIEW

elimination half-life of the inhibitor. Dissociation of a reversible inhibitor from an enzyme is described by the equilibrium dissociation constant K i . Equations describing each form of reversible inhibition are shown in Figure 1. 8 of 27

## Competitive Inhibition

## Non-competitive Inhibition

<!-- image -->

Lineweaver

Burk

<!-- image -->

<!-- image -->

## Uncompetitive Inhibition

Mixed Inhibition

<!-- image -->

<!-- image -->

Lineweaver

Burk

<!-- image -->

Figure 1. Enzyme kinetics of reversible inhibition. Characteristic Michaelis-Menten curves and equations are shown with their corresponding Lineweaver-Burk plots for competitive inhibition (blue), non-competitive inhibition (yellow), uncompetitive inhibition (pink), and mixed competitive/non-competitive inhibition (green). Filled circles represent metabolite formation rates measFigure 1. Enzyme kinetics of reversible inhibition. Characteristic Michaelis-Menten curves and equations are shown with their corresponding Lineweaver-Burk plots for competitive inhibition (blue), non-competitive inhibition (yellow), uncompetitive inhibition (pink), and mixed competitive/noncompetitive inhibition (green). Filled circles represent metabolite formation rates measured without

<!-- image -->

ured without an inhibitor, and open circles represent metabolite formation rates measured with an

Michaelis

Menten

<!-- image -->

Lineweaver

Burk

an inhibitor, and open circles represent metabolite formation rates measured with an inhibitor. v = the rate of metabolite formation, Vmax = the maximal rate of metabolite formation, Km = the substrate concentration at the half-maximal rate of metabolite formation, [I] = inhibitor concentration, [S] = probe substrate concentration, K i = the equilibrium dissociation constant for the enzymeinhibitor complex, α K i = the equilibrium dissociation constant for the enzyme-substrate-inhibitor complex. Dashed lines in the Lineweaver-Burk plots indicate x = 0 (vertical dashed line) and y = 0 (horizontal dashed line). Figure adapted from Ring et al. using GraphPad Prism version 10.1.2 software [102].

Generally considered the most common and well-understood form of inhibition, competitive inhibition occurs when two molecules 'compete' for mutually exclusive, reversible binding at the same active site of a CYP enzyme, thereby reducing the amount of enzyme available to metabolize a drug when a competitive inhibitor is present [102,103]. Though the Vmax of the reaction is unaffected, the Km is increased as a result of competition for the same active site [104]. Non-competitive inhibition occurs when an inhibitor is capable of binding at an allosteric site, regardless of whether a substrate is bound in the active site [102]. Substrates may still bind to the active site following non-competitive binding; however, the resulting enzyme-substrate-inhibitor complex is inactive [103]. Since non-competitive inhibitors do not impact substrate binding, the Km remains unchanged while the Vmax decreases as a consequence of inhibition [102,104]. An uncompetitive inhibitor lacks affinity for the free enzyme and is only capable of binding at an allosteric site when the enzyme is bound to the substrate (i.e., the enzyme-substrate complex) [102,103]. Like non-competitive inhibition, the enzyme-substrate-inhibitor complex is rendered inactive [103]. Uncompetitive inhibitors reduce the Vmax of the reaction by reducing the number of functional enzyme-substrate complexes, which leads to a corresponding decrease in Km as the reaction seeks equilibrium [102]. Mixed competitive/non-competitive inhibition (commonly referred to as simply 'mixed inhibition') is a distinct type of noncompetitive inhibition, in which the inhibitor binds to the allosteric site with varying affinity based on whether a substrate is bound in the active site by a factor α [102]. This necessitates two terms for inhibitor dissociation when describing mixed inhibition kinetics: K i for dissociation of the inhibitor from the enzyme-inhibitor complex, and α K i for dissociation of the inhibitor from the enzyme-substrate-inhibitor complex [102]. As a result, mixed inhibitors decrease the Vmax of the reaction and may either increase or decrease the Km depending on the value of α [102].

The type of reversible inhibition enacted by an inhibitor may be identified experimentally using classic Michaelis-Menten enzyme kinetic experiments for determining the Vmax and the Km with and without the inhibitor [102,104]. Using these results, graphing the inverse of the measured metabolite formation rate vs. the inverse of the substrate concentration generates a Lineweaver-Burk plot. Each type of reversible inhibition is associated with a characteristic shift in the resulting Michaelis-Menten and Lineweaver-Burk plots, shown in Figure 1. Historically, the enzyme kinetic constants and mechanism of inhibition were determined by visually examining the shift in slope (equal to Km/Vmax), x-intercept (equal to -1/Km), and y-intercept (equal to 1/Vmax) observed with an inhibitor on the Lineweaver-Burk plot [104]. Today, the most accurate and preferred method for determining kinetic constants is to use nonlinear regression to fit the Michaelis-Menten model directly to the non-transformed data [102]. The type of inhibition may then be identified by determining which reversible inhibition model best fits the experimental data (represented by the equations in Figure 1). These analyses may be performed using one of many widely accepted statistical software packages, such as GraphPad Prism.

Importantly, experiment conditions should be optimized prior to performing enzyme kinetic experiments for inhibition. To accurately measure kinetic parameters, the linearity of metabolite formation with respect to both incubation time and protein concentration must be established beforehand. These experiments should be performed using a sub-

strate concentration approaching the Km. The shortest incubation time and lowest protein concentration within the linear range should be selected for performing kinetic experiments to minimize depletion of the substrate [102]. The concentration of inhibitor should approximate the in vivo concentration at the CYP active site [102].

The degree of reversible inhibition may be measured as a ratio of intrinsic clearance values for a probe CYP substrate in the presence and absence of the interacting drug. This ratio is referred to as the R 1 value and is calculated as follows:

R 1 = 1 + Imax,u K i,u

where Imax,u is the maximal unbound plasma concentration of the interacting drug at steady state, and K i .u is the in vitro unbound inhibitor dissociation constant [5]. If R 1 is ≥ 1.02, further investigation using predictive modeling techniques or a clinical DDI study is warranted [5,105].

Reversible inhibition may be differentiated from other forms of inhibition in vitro by determining the effect of preincubating the inhibitor with the CYP enzyme before adding the substrate to reactions. Irreversible inhibitors display time-dependent, saturable kinetics, and the length of the preincubation period correlates with the degree of inhibition [103]. In contrast, the degree of reversible inhibition is unaffected by preincubation time. Time-dependent inhibitors are thus defined by an observed increase in the extent of inhibition when a preincubation period is added to reactions [103,106]. Time-dependent and mechanism-based inhibition are closely related but separately defined terms. Whereas time-dependent inhibitors are identified by the kinetics of enzyme inhibition experimentally, mechanism-based inhibition is a type of time-dependent inhibition where the inhibitor binds to the active site and subsequently inactivates the enzyme [106].

To experimentally determine whether a compound is a time-dependent inhibitor, probe substrate assays are performed with the addition of a preincubation step [106,107]. This is typically accomplished using what is commonly known as the 'dilution method', in which the inhibitor is first preincubated with a high concentration of CYP enzyme(s) and NADPH. Aliquots of this incubation are then diluted into a second incubation containing the substrate and NADPH at specified time points. These incubations are performed using a range of inhibitor concentrations to determine the k inact and K i values [106]. The resulting rates of metabolite formation can then be compared to matched incubations without inhibitors to determine the degree of time-dependent inhibition [106,107]. The latest FDA guidance for industry on in vitro drug interaction studies recommends screening for both reversible and time-dependent inhibition of CYP1A2, CYP2B6, CYP2C8, CYP2C9, CYP2C19, CYP2D6, and CYP3A [5]. The decision tree presented in Figure 2 illustrates the process for evaluating CYP inhibition for new lead compounds.

## 3.1.2. Quasi-Irreversible Inhibition

Some substrates are transformed by CYPs into metabolite intermediates that form stable, inactive complexes with the prosthetic heme group of the enzyme, known as a metabolite intermediate complex. Metabolite intermediate complexes are stable at physiologic conditions and can be detected experimentally using imaging spectroscopy [61,106,108]. This process is called quasi-irreversible inhibition because decomplexation can technically occur in the presence of lipophilic compounds that can displace the intermediate and restore activity in vitro [103,109]. Incubation with the oxidizing agent potassium ferricyanide can be performed to recover enzyme activity following quasi-irreversible inhibition [109,110]. In this context, decomplexation refers to displacement of the metabolic intermediate from the iron-containing coordination complex (i.e., the heme group) located in the active site of CYP enzymes [103,111].

without inhibitors to determine the degree of time-dependent inhibition [106,107]. The

latest FDA guidance for industry on in vitro drug interaction studies recommends screen-

ing for both reversible and time-dependent inhibition of CYP1A2, CYP2B6, CYP2C8,

CYP2C9, CYP2C19, CYP2D6, and CYP3A [5]. The decision tree presented in Figure 2 il-

lustrates the process for evaluating CYP inhibition for new lead compounds.

Figure 2. Decision tree for studying CYP inhibition in vitro. Decision nodes are based on the 2020 FDA Guidance for Industry for in vitro drug interactions [5]. HTS = high throughput screening, CYP = cytochrome P450, HLM = human liver microsome, LCMS = liquid chromatography-mass spectrometry, DDI = drug-drug interaction. Figure 2. Decision tree for studying CYP inhibition in vitro. Decision nodes are based on the 2020 FDA Guidance for Industry for in vitro drug interactions [5]. HTS = high throughput screening, CYP = cytochrome P450, HLM = human liver microsome, LCMS = liquid chromatography-mass spectrometry, DDI = drug-drug interaction.

<!-- image -->

## 3.1.3. Irreversible Inhibition

3.1.2. Quasi-Irreversible Inhibition

Some substrates are transformed by CYPs into metabolite intermediates that form stable, inactive complexes with the prosthetic heme group of the enzyme, known as a metabolite intermediate complex. Metabolite intermediate complexes are stable at physiologic  conditions  and  can  be  detected  experimentally  using  imaging  spectroscopy [61,106,108]. This process is called quasi-irreversible inhibition because decomplexation can technically occur in the presence of lipophilic compounds that can displace the intermediate and restore activity in vitro [103,109]. Incubation with the oxidizing agent potassium ferricyanide can be performed to recover enzyme activity following quasi-irreversible inhibition [109,110]. In this context, decomplexation refers to displacement of the metabolic intermediate from the iron-containing coordination complex (i.e., the heme group) Irreversible inhibition occurs when an inhibitor irreversibly inactivates a CYP enzyme, typically either through alkylation of the heme moiety or covalent binding to apoprotein (i.e., protein without a bound cofactor) [103]. Since this form of inhibition relies on metabolic activation, it is also commonly referred to as mechanism-based or suicide inhibition [103]. Importantly, so-called irreversible inhibition does not always result in complete loss of CYP enzyme activity. In some cases, covalent binding may be reversible, and activity may return over time [111]. Examples of reversible covalent inhibitors include the anticancer agent bortezomib, which reversibly inhibits the 26S proteasome by binding to a threonine residue in its catalytic site, and the antidiabetic agent saxagliptin, which covalently modifies a serine residue in the active site of dipeptyl peptidase-4 [112]. In other cases, the dissociation rate constant k off for the substrate or the resulting metabolite is very small, causing de facto irreversible inhibition [103,113].

located in the active site of CYP enzymes [103,111]. Restoration of enzyme activity following irreversible inhibition is typically based on the rate at which the affected tissue(s) synthesize new CYP proteins. The estimated recovery half-life for different CYP enzymes has ranged from 20 to 50 h depending on the individual enzyme affected and the elimination half-life of the inhibitor tested [114,115].

Like the R 1 value for reversible inhibition, the R 2 value for estimating the degree of time-dependent inhibition is determined as a ratio [105]. The R 2 value is calculated

using the natural in vivo enzyme degradation rate constant (k deg ) [106] and the observed inactivation rate of the affected enzyme (k obs ):

R 2 = k obs + k deg k deg

K obs may be calculated using the maximal inactivation rate constant (k inact ), the unbound inhibitor concentration at half-maximal inactivation (K I,u ), and maximal unbound plasma concentration of the interacting drug at steady state (Imax,u) [5]:

k obs = k inact × 50 × I max,u K I,u + 50 × Imax,u

If R 2 is ≥ 1.25, the FDA recommends further investigation of the drug's interaction potential using model-based predictions or clinical DDI studies using a clinical index substrate [5].

## 3.2. Methods for Assessing CYP Inhibition

## 3.2.1. Early High-Throughput Screening

Plate-based fluorescent and luminescent assays can be used in early high throughput screening to determine a drug's inhibitory potential. These experiments typically involve dosing rCYPs in a 96-well format with a pro-fluorescent or pro-luminescent substrate that generates metabolites that can be detected using a plate reader. The IC 50 value (the concentration of inhibitor resulting in half-maximal inhibition) may then be calculated by measuring the difference in signal with a range of inhibitor concentrations compared to control incubations [116-118]. While such assays offer the advantage of high throughput and sensitivity, they are typically only performed with rCYPs since these substrates are not selective for individual CYP enzymes [117,119]. Furthermore, the assay must reliably yield metabolites with an attached fluorophore to avoid non-specific fluorescence.

Cocktails containing multiple selective CYP substrates are also commonly used with microsomes to increase throughput in combination with LC-MS metabolite profiling to screen for inhibition of multiple CYPs at once [116,119]. The Basel cocktail, for example, has been validated for both in vitro and in vivo DDI studies, and contains the following CYP substrates: caffeine (CYP1A2), efavirenz (CYP2B6), losartan (CYP2C9), omeprazole (CYP2C19), metoprolol (CYP2D6), and midazolam (CYP3A) [120].

One additional method is the use of radiolabeled selective CYP substrates, which typically release radiolabeled water or formaldehyde when metabolized [116,117,121]. This approach requires solid phase extraction or scintillation proximity assay beads to isolate radioactive metabolites [116,117,121].

## 3.2.2. Probe Assays for CYP Inhibition

Following initial screening, validated probe assays with HLM are commonly performed prior to and/or alongside phase I studies. A comprehensive list of both in vitro and clinical index substrates, inhibitors, and inducers for major CYP enzymes and transporters has been published by the U.S. FDA for DDI screening (see Table 1 for CYP enzymes) [82]. Importantly, these marker substrate reactions, while useful, are accompanied by several limitations. Although these studies are considered the industry standard for measuring drug inhibition, few (if any) substrates are fully selective for a single CYP enzyme. Often, multiple metabolites are formed simultaneously through multiple pathways, which may affect results if the inhibitor is also metabolized by one or more of the same enzymes as the substrate. Drug metabolites may also inhibit CYPs to an equal or greater extent than the parent drug [122]. Investigators should consider these factors beforehand and select an alternative CYP substrate for microsomal studies if needed. This issue may be partially circumvented by using individual rCYP enzymes, though this system comes with its own set of limitations. Kinetic parameters calculated using recombinant enzymes may show a

lack of correlation to those calculated using microsomes due in part to over-expression of the enzyme and the lack of additional drug-metabolizing enzymes. Further validation with microsomes is recommended after initial screening with recombinant enzymes [123].

In addition, drug-metabolizing enzymes, particularly those in the CYP3A subfamily, mayhave flexible active sites that can be inhibited through different mechanisms depending on the structure of the bound substrate [124]. Inhibition of CYP3A enzymes should ideally be assessed using two different marker reactions (typically midazolam 1 ' -hydroxylation, testosterone 6 β -hydroxylation, and/or felodipine dehydrogenation). Additional considerations for substrate selection include the rate of metabolite generation in vitro and the availability of metabolite standards and internal standards for LC-MS analysis [5,119,124].

For clinical DDI studies, an ideal index substrate is sensitive enough to demonstrate measurable changes in exposure when administered with an inhibitor. The AUC of a sensitive index substrate should increase by at least five-fold with a strong inhibitor, and moderately sensitive substrates should demonstrate an AUC increase of two to five-fold with a strong inhibitor [5].

## 3.2.3. Model-Based Approaches for Predicting CYP Inhibition

The recent adoption of high throughput screening in DDI assessment has led to the use of predictive modeling to analyze large datasets for potential CYP-mediated DDIs. In silico prediction of CYP-mediated metabolism carries several advantages over traditional in vitro approaches: modeling may be performed very early in drug development to quickly assess many compounds at a low cost [125]. In addition, modeling may be performed with compounds that have yet to be synthesized [125].

Predictive models are commonly developed using a ligand- and/or structure-based approach and validated through cross-validation or with large external datasets of known substrates and inhibitors [125-127]. Following a ligand-based approach, large databases of structurally diverse compounds are screened for binding and inhibition of CYPs based on quantitative structure-activity relationships [125]. Structure-based models instead rely on three-dimensional CYP protein structures obtained through x-ray crystallography or NMR, and predictions are made based on docking simulations [125,128]. For both model types, multiple linear regression and/or machine learning techniques are used to make predictions [125].

## 4. CYP Induction

## 4.1. Mechanisms of CYP Induction

Enzyme induction refers to a mechanism characterized by increased expression and activity of an enzyme resulting from exposure to a xenobiotic or endogenous inducing agent [129]. The increased clearance of the drug results in lower concentrations and may lead to a diminished pharmacological effect [2]. For example, concomitant treatment with rifampin reduced both plasma concentrations of sulfonylureas and their blood glucose lowering effect possibly due to induction of CYP2C9 [130,131]. Induction of P-glycoprotein by rifampin might have also contributed to the reduced concentrations and effectiveness of the drugs [130,131]. In addition, although induction is generally considered less of a risk compared to inhibition, the increased metabolism of the victim drug can result in the formation of toxic metabolites [2].

Unlike CYP inhibition, which can rapidly affect drug metabolism by blocking the enzyme activity, CYP enzyme induction is a slower process [132]. CYP induction involves the upregulation of the enzyme biosynthesis, which takes time to reach a new steadystate level [132]. CYP induction by exogenous compounds is mainly mediated by three receptor-dependent mechanisms that can activate transcription of the genes that encode CYP families 1-3 [133,134]. These receptors include aryl hydrocarbon receptor (AhR), which belongs to the basic-helix-loop-helix-Per-Arnt-Sim (bHLH-PAS) family, pregnane X receptor (PXR), and constitutive androstane receptor (CAR) [2,133,135]. In the absence of ligands, these receptors exist in a latent state in the cytoplasm bound to heat shock protein

90 (Hsp90). When bound to ligands, the receptors undergo a conformational change in the ligand-binding domain, leading to the release of Hsp90, activation, and translocation to the nucleus for transcription (described in more details below).

In addition to AhR-, PXR-, and CAR-dependent mechanisms, other mechanisms have been implicated in CYP induction. For example, direct and indirect glucocorticoid receptormediated CYP induction have been reported in various studies [34,136,137]. Moreover, some CYPs are regulated at the level of mRNA and protein stabilization [138-140]. These transcriptional and post-transcriptional mechanisms are well reviewed in [141-143].

## 4.1.1. Aryl Hydrocarbon Receptor

Extensive studies in the past two decades have identified many natural dietary and endogenous ligands of AhR and unmasked various physiological functions in normal development and homeostasis [144-146]. However, most AhR ligands are toxic xenobiotics, including halogenated aromatic hydrocarbons and polycyclic aromatic hydrocarbons [134,145]. In addition, AhR binds with several pharmaceuticals that are used clinically for multiple disorders [147]. Ligand binding mediates translocation of AhR to the nucleus where it heterodimerizes with another bHLH-PAS protein AhR nuclear translocator (ARNT) [132,134]. The AhR-ARNT complex associates with the xenobiotic response elements (XRE) in the promoter of target genes and recruits coactivators, such as SRC-1, CBP/p300, and NCOA-2 [134].

AhRis broadly distributed in human tissues, with its highest expression in the placenta, lung, heart, pancreas, and liver [148]. AhR primarily regulates CYP1A1 and CYP1B1 in extrahepatic tissues, while it targets CYP1A2 in the liver [149]. Generally, CYP1A1 displays much higher sensitivity to AhR inducers compared to CYP1A2 and CYP1B1, which may be attributed to the presence of multiple XRE sites in CYP1A1 [132,134]. In addition to CYP1, AhR has been shown to regulate some members in the CYP2 family [150-152]. However, it is important to note that there are species-specific differences. For example, Cyp2a5 is regulated by AhR in mice, though there is currently no equivalent evidence supporting the regulation of its human ortholog CYP2A6 [150].

## 4.1.2. Nuclear Receptors

NRs are ligand-regulated transcription factors that regulate many physiological processes such as metabolism, inflammation, reproduction, and cell growth. A number of NRs have been identified as playing a role in regulating the expression of CYPs in response to xenobiotics. PXR and CAR are two well-studied NRs that serve as central regulators of CYPs. Both PXR and CAR have a ligand-binding domain that can bind a wide variety of ligands. Particularly, the ligand-binding domain of PXR is very large (1200-1600 Å 3 ), highly hydrophobic, and flexible [153-155]. This unique structural feature enables it to bind a wide variety of molecules with varying size and structure, and allows a single ligand to engage in multiple orientations. Although the ligand-binding domain of CAR is hydrophobic, it is smaller (~600 Å 3 ) and less flexible compared to that of PXR [155], making the receptor activated with a smaller number of ligands.

The DNA-binding domain and ligand-binding domain of NRs exhibit a high degree of homology and conservation across the species. However, the ligand-binding domain of PXR is significantly different across the species. Human, mouse, rat, and rabbit PXR orthologues show 75-82% amino acid sequence identity in their ligand-binding domain [156-158]. Similarly, the human and rodent CAR share ~70% sequence identity in their ligand-binding domain [159]. The poor homology among species is thought to lead to the marked species variation in ligand preferences and the induction of CYPs [156-158]. For example, rifampicin exhibited minimal activity when interacting with mouse PXR, but was a highly efficient activator of human PXR [160]. Conversely, activation of mouse PXR by pregnenolone 16 α -carbonitrile was approximately three-fold higher compared to human PXR activation. Similar to PXR, studies demonstrated variation in ligand preferences of CAR across the species. 6-(4-chlorophenyl)imidazo[2,1-b][1,3]thiazole-5-

arbaldehyde-O-(3,4-dichlorobenzyl)oxime (CITCO) activates CAR in humans but not in mice [161]. In contrast, 1,4-bis-[2-(3,5-dichloropyridyloxy)]benzene,3,3 ' ,5,5 ' -tetrachloro-1,4bis(pyridyloxy)benzene (TCPOBOP) is a stronger inducer for mouse CAR than human CAR [159,162]. To overcome the species differences in ligand recognition for translation of in vivo results from animal models to humans, various humanized mouse models for PXR, CAR, and CYPs have been developed [163-166].

In humans, both PXR and CAR are predominantly expressed in the liver with minimal levels detected in other tissues [142,167,168]. PXR regulates expression of several members in the subfamilies of CYP2A , CYP2B , CYP2C , and CYP3A [132,134,142]. Among these members, regulation of CYP3A4 by PXR has been studied extensively [169-171]. Following translocation to the nucleus, PXR dimerizes with another NR retinoid X receptor (RXR) and then the PXR-RXR complex binds to AG(G/T) TCA-like direct repeats separated by three or four bases (DR3 and DR4), along with an everted repeat separated by 6 bases (ER6) [170]. These binding interactions occur at several distinct sites on the CYP3A4 gene, including ER6 in the proximal promoter, DR3 in the xenobiotic-response element module (XREM), ER6 in a distal enhancer module, and the DR4 motif [169-171]. The DNA-bound PXR-RXR complex then activates transcription through recruitment of multiple coactivators including SRC-1, p300, and PGC-1 [134]. Similar to PXR, CAR forms a heterodimer complex with RXR in the nucleus. CAR-RXR complex regulates expression of the CYP2B gene by binding to DR4 motifs in the XREM [172]. Several coactivators of CAR, such as SRC-1, PGC-1, and ASC-2, have been identified [173].

## 4.1.3. Crosstalk between Receptors

The significance of the interplay between receptor signaling pathways in CYP expression has been widely studied. This coregulation by receptors can occur at three levels: (i) sharing common ligands, (ii) receptor-receptor interactions, and (iii) sharing DNAbinding elements [134]. Notably, PXR and CAR have been associated with their involvement in mediating the effects of xenobiotics on the expression of CYP2B6 and CYP3A4 . For example, rifampicin, a potent PXR ligand and CYP3A4 inducer, has been shown to induce CYP2B6 in primary human hepatocytes. This induction is associated with the binding of PXR to the response elements in the CYP2B6 gene [174,175]. In healthy volunteers taking a single dose of efavirenz, rifampicin enhanced CYP2B6-mediated efavirenz 8-hydroxylation and decreased the AUC of efavirenz. [176]. However, in vitro experiments demonstrated that CYP3A4 is more sensitive to induction by rifampicin than CYP2B6 [177]. Conversely, CAR can induce CYP3A4 expression by binding to the distal XREM and promoter proximal regions of the gene [169]. In addition, Fahmi et al. demonstrated co-induction of CYP3A4 with various CYP2B6 inducers [177].

A recent study showed that PXR also interacts with AhR to regulate CYP expression [178]. The expression of PXR mRNA was diminished when primary hepatocytes were exposed to the AhR ligand, 2,3,7,8-tetrachlorodibenzo-p-dioxin (TCDD). Furthermore, rifampicin-induced CYP3A4 expression was reduced in the presence of TCDD, suggesting a negative regulatory effect of AhR on CYP3A4 expression. However, the mechanisms by which AhR activation regulates the expression of PXR and CYP3A4 are still not clear.

## 4.2. Methods for Assessing CYP Induction

## 4.2.1. Primary Human Hepatocytes

Cultured primary human hepatocytes express all the relevant hepatic metabolic enzymes, transporters, and their regulators [134]. Among the various in vitro or cell-based approaches, the use of primary hepatocytes is recommended by the FDA and EMA as these cells provide results that are closest to in vivo studies [2,134]. During drug development, initial experiments can be conducted to evaluate CYP1A2, CYP2B6, and CYP3A4/5 [5]. If CYP3A4/5 induction is positive, however, the potential of CYP2C induction by the test drug should be evaluated in the follow-up studies since both CYP3A4/5 and CYP2C enzymes are induced by PXR activation [2]. The incubation duration for inducers typically

ranges from 48 to 72 h, which allows the complete induction of enzyme. During the incubation period, the inducer is added daily by replacing the medium containing the drug. Commonly used CYP inducers are presented in Table 1. The standard endpoints involve the measurement of mRNA levels and/or enzyme activity.

In general, the fold change in mRNA and enzyme activity measurements are thought to be consistent with each other [129]. However, a major challenge with enzyme activity assays is the potential for mixed outcomes when the test compound acts as both inducer and inhibitor [5]. For example, primary human hepatocytes exposed to DPC 681, a selective human immunodeficiency virus (HIV) protease inhibitor, had significant increases in CYP3A4 mRNA and protein levels [179,180]. However, CYP3A4 metabolic activity did not increase due to the inhibition effect of DPC 681. To address this challenge, assessment of induction using transcriptional analysis through mRNA measurement is recommended by the FDA [5]. The test compound can be considered as an inducer when there is a dose-dependent increase in mRNA expression that exceeds two-fold compared to the vehicle control or if the mRNA reaches at least 20% of the level observed in the positive control treated with known inducers. In addition, it is important to validate the system by generating full dose response curves of the positive controls to show that CYP enzymes are functional and inducible. Examples of positive controls include 20 µ Mof omeprazole, 1 mM of phenobarbital, and 10 µ M of rifampicin for CYP1A2, CYP2B6, and CYP3A4, respectively [2].

As follow-up to any dose-dependent positive response, definitive studies can be conducted to determine the Emax (maximum induction effect) and EC 50 (concentration causing half-maximal effect). During drug development, these studies must be conducted in primary human hepatocytes from at least three individual donors to address variability in individual responses to inducers [2,3]. Multiple concentrations of the test compound, usually 4 to 8, covering up to one order of magnitude (10 × ) over the Cmax are typically used. Once the Emax and EC 50 are determined, several approaches can be used for further prediction of enzyme induction [181,182]. The basic kinetic model involves a direct comparison of values determined from the in vitro Emax, EC 50 , and plasma concentration of test compounds with the uniform threshold of DDI risk [181]. In this approach, a positive induction is determined by the formula:

<!-- image -->

where Imax,u is the maximal unbound inducer plasma concentration at steady state, and d is the induction scaling factor [5]. Correlation methods determine the magnitude of the inducible effect according to a calibration curve of relative induction score (RIS score, (Emax × [I]/(EC 50 + [I]))) with known inducers or Imax,u/EC 50 with known inducers and non-inducers. The advantages and disadvantages of each approach are described in [181].

Using primary human hepatocytes in induction assays has several limitations, including donor variability, limited availability, short viability, and batch-to-batch variation [132,183,184]. The major concern with 2D monolayer primary hepatocyte cultures is the rapid de-differentiation after plating and loss of hepatic functions, including drug metabolizing enzyme activity [183,185]. Several cell models have been developed to prevent or ameliorate the de-differentiation [186-188]. Overlaying 2D cultures with a thin layer of extracellular matrix (ECM) improves cellular phenotypes and polarization [186]. However, a decline in CYP3A activity, along with a decline in albumin secretion and urea production, was demonstrated after two weeks in culture [187]. The 3D spheroid primary hepatocytes have been suggested as an emerging tool to study drug metabolism as they maintain in vivo hepatic characteristics and stably express CYPs for several weeks in culture [188]. Furthermore, a recent study by Järvinen et al. demonstrated that mRNA and protein levels of CYPs are induced by different inducers in spheroids [189]. A major limitation associated with using spheroids is that not all batches of primary hepatocytes have the capacity to develop into spheroids [189].

## 4.2.2. Immortalized Hepatocytes

Immortalized hepatic cell models offer several advantages for CYP induction studies over primary hepatocytes: easy accessibility, low variability, highly reproducible results in response to inducers, and high availability. Simian virus 40 immortalized human hepatic Fa2N-4 cells express CYP1A2, CYP2C9, and CYP3A4 protein, and the mRNA expression and activity of these enzymes are inducible in response to prototypical inducers [190]. In addition, Ripp et al. demonstrated a comparable increase in mRNA levels of CYP3A4 using 24 compounds in Fa2N-4 cells and primary human hepatocytes [191]. However, CARselective activators CITCO and artemisinin did not induce CYP3A4 and CYP2B6 mRNA levels, possibly due to very low expression of CAR in Fa2N-4 cells [192]. Furthermore, rifampicin resulted in a 10-fold higher EC 50 in Fa2N-4 cells than cryopreserved human hepatocytes, possibly due to low expression of the hepatic uptake transporters organic anion-transporting polypeptides OATP1B1 and OATP1B3 [192].

HepaRG is a human hepatoma cell line that expresses the major CYPs and their regulators including CAR at levels similar to those observed in freshly isolated hepatocytes after differentiation with DMSO [183,193]. HepaRG cells respond to prototypical inducers of CYP1A1, CYP1A2, CYP2B6, CYP2C8, CYP2C9, CYP2C19, and CYP3A4 at both mRNA and enzyme activity levels [193-196]. A strong correlation between EC 50 for CYP3A4 induction following rifampicin treatment has been demonstrated in HepaRG cells and primary human hepatocytes [196]. Furthermore, studies showed that the results from HepaRG cells can be used to predict the in vivo induction effect of drugs using different calculation models [195,197,198]. These indicate that HepaRG cells are an excellent surrogate for predicting CYP3A induction potential by drugs in primary hepatocytes and in vivo.

## 4.2.3. High Throughput Assays

PXR receptor assays are widely used high throughput assays due to their importance in DDI studies. The cell-free ligand binding assays typically involve quantification of the competition between the test compound and a radiolabeled ligand for receptor binding in genetically expressed and isolated receptor preparations. However, there are instances in which substantial ligand-receptor binding fails to trigger transactivation, resulting in false positives. On the other hand, cell-based transactivation assays are more accurate with less false positives and better correlate with human DDIs [3]. In the transactivation assays, two expression vectors, full length human PXR and a variation of the target promoter coupled to a reporter such as luciferase, are transfected into host cells [3,183]. Host cells are then treated with the test compound, and the reporter gene activity is assayed. Increased reporter gene activity is an indication of induction, and a dose-response curve is generated to determine Emax and EC 50 [3,133].

These assays offer several advantages over using cultured cells, including their simplicity to conduct, high capacity, and cost-effectiveness [134,183]. Consequently, they can be particularly beneficial in the early phase of drug discovery [183]. However, one major limitation is their capacity to assess only one receptor-mediated induction pathway at a time, as crosstalk between receptors can activate the same target genes [3]. In addition, the cell-free ligand binding assays are unable to account for other mechanisms such as the impact of cell membrane, which may restrict cellular uptake of drugs [3,134].

## 5. Additional Considerations for Drug Interactions

As noted above, CYPs are involved in the metabolism of approximately 70-80% of small molecule drugs in clinical use [7,199]. For this reason, CYPs are frequently involved in DDIs because co-administered drugs are often substrates, inducers, and/or inhibitors of CYPs. Human CYP enzymes of the 1, 2, and 3 families play a major role in drug metabolism. These enzymes include CYP1A2, CYP2B6, CYP2C9, CYP2C8, CYP2C19, CYP2D6, CYP3A4, and CYP3A5. CYP3A4 is the most abundant CYP in adult human liver and intestine, and this enzyme is involved in the metabolism of approximately 50% of small molecule drugs in clinical use or in development [199,200]. The large flexible active site of CYP3A4 and its

major role in drug metabolism make it particularly susceptible to DDIs [201]. Further, more than one ligand can occupy the CYP3A4 active site at one time [201]. In addition to DDIs, drug interactions can involve ingested or inhaled xenobiotics, such as ethanol (CYP2E1 inducer) and tobacco smoke (CYP1A1 and CYP1A2 inducer); herbal supplements, such as St. John's Wort (CYP3A4 inducer); and food, such as components of grapefruit juice (CYP3A4 inhibitor) [199]. Beyond the drug-metabolizing CYPs, other CYP enzymes are involved in the metabolism of steroids (e.g., CYP7A1), fatty acids (e.g., CYP4A11), and vitamins (e.g., CYP26A1). Still other CYP enzymes currently have no known substrates (i.e., 'orphan' CYPs) [199].

Drug interaction studies can be complicated by the fact that some drugs can induce more than one CYP enzyme, and some drugs can inhibit more than one CYP enzyme. Some examples are provided below. First, as noted above, rifampicin is an agonist of the nuclear receptor PXR. PXR regulates the expression of multiple CYP enzymes and drug transporters [202]. CYP enzymes induced by rifampicin include CYP2B6, CYP2C8, CYP2C9, CYP2C19, and CYP3A4 [82]. Rifampicin also induces P-glycoprotein [203]. In addition, rifampicin can inhibit the transporters organic anion transporting polypeptide (OATP) 1B1 and OATP1B3. DDIs involving rifampicin are an important clinical concern [203]. Second, azole antifungals are a common cause of drug interactions due to CYP inhibition. The selectivity of CYP inhibition depends on the concentration of inhibitor [68]. For example, ketoconazole is a potent inhibitor of CYP3A4 and CYP3A5 at nanomolar concentrations in vitro [204]. At higher concentrations, ketoconazole can inhibit other CYP enzymes. In addition, some drugs inhibit multiple CYP enzymes at therapeutically relevant concentrations. For example, fluconazole is a strong inhibitor of CYP2C19 and a moderate inhibitor of CYP2C9 and CYP3A4 [82]. Therefore, DDIs with fluconazole are a concern in clinical practice [205]. Additionally, a compound can have different effects on the activity of CYP enzymes. For example, α -naphthoflavone is an inhibitor of CYP1A2 and an activator of CYP3A4 [206].

Atypical (non-Michaelis-Menten) kinetic profiles have been reported for CYP enzymes, which may be characterized by sigmoidal autoactivation, substrate inhibition, or biphasic kinetic profiles [207]. In addition, experimental conditions, such as nonspecific binding of substrate to microsomal preparations, may result in the appearance of 'atypical' kinetic profiles, which are artifacts of the experimental set-up [207]. The impact of in vitro observed atypical kinetic profiles on IVIVE and DDI predictions requires further investigation [208].

## 6. Conclusions

Multiple drug therapy is becoming increasingly more common to enhance therapeutic efficacy. Many drugs undergo hepatic metabolism by CYP enzymes for clearance from the body. Over the years, significant advancements have been achieved on in vitro CYP assays and predictions for DDIs. The information gathered from in vitro studies not only helps in the identification of risks associated with multiple drug therapy but also provides insights into the fundamental mechanisms driving these interactions. While in vitro DDI assessment has advanced our understanding, challenges persist, including the need for standardized protocols, consideration of interindividual variation, and the incorporation of physiologically relevant conditions. Future research should focus on refining methodologies, fostering the development of more predictive models that closely mirror the complexities of in vivo interactions.

Author Contributions: Conceptualization, J.L., J.L.B. and R.M.G.; writing-original draft preparation, J.L., J.L.B. and R.M.G.; writing-review and editing, J.L., J.L.B., R.M.G. and K.D.J.; visualization, J.L. and J.L.B.; supervision, K.D.J.; funding acquisition, J.L.B. and K.D.J. All authors have read and agreed to the published version of the manuscript.

Funding: K.D.J. was supported by the National Institutes of Health National Institute of General Medical Sciences (award R35GM143044). J.L.B. was supported by the National Institute of General Medical Sciences of the National Institutes of Health (award T32GM086330). This review is solely

the responsibility of the authors and does not necessarily represent the official views of the National Institutes of Health.

Conflicts of Interest: The authors declare no conflicts of interest.

## References

- 1. Tornio, A.; Filppula, A.M.; Niemi, M.; Backman, J.T. Clinical Studies on Drug-Drug Interactions Involving Metabolism and Transport: Methodology, Pitfalls, and Interpretation. Clin. Pharmacol. Ther. 2019 , 105 , 1345-1361. [CrossRef] [PubMed]
- 2. Lu, C.; Di, L. In vitro and in vivo methods to assess pharmacokinetic drug- drug interactions in drug discovery and development. Biopharm. Drug Dispos. 2020 , 41 , 3-31. [CrossRef]
- 3. Sinz, M.; Wallace, G.; Sahi, J. Current industrial practices in assessing CYP450 enzyme induction: Preclinical and clinical. AAPS J. 2008 , 10 , 391-400. [CrossRef]
- 4. Wienkers, L.C.; Heath, T.G. Predicting in vivo drug interactions from in vitro drug discovery data. Nat. Rev. Drug Discov. 2005 , 4 , 825-833. [CrossRef] [PubMed]
- 5. In Vitro Drug Interaction Studies-Cytochrome P450 Enzyme- and Transporter-Mediated Drug Interactions Guidance for Industry ; U.S. Food and Drug Administration: Silver Spring, MD, USA, 2020.
- 6. Sun, L.; Mi, K.; Hou, Y.; Hui, T.; Zhang, L.; Tao, Y.; Liu, Z.; Huang, L. Pharmacokinetic and Pharmacodynamic Drug-Drug Interactions: Research Methods and Applications. Metabolites 2023 , 13 , 897. [CrossRef]

7.

Zanger, U.M.; Schwab, M. Cytochrome P450 enzymes in drug metabolism: Regulation of gene expression, enzyme activities, and

impact of genetic variation.

Pharmacol. Ther.

2013

,

138

, 103-141. [CrossRef] [PubMed]

- 8. Yoshida, K.; Maeda, K.; Sugiyama, Y. Hepatic and intestinal drug transporters: Prediction of pharmacokinetic effects caused by drug-drug interactions and genetic polymorphisms. Annu. Rev. Pharmacol. Toxicol. 2013 , 53 , 581-612. [CrossRef]
- 9. Kot, M.; Daniel, W.A. The relative contribution of human cytochrome P450 isoforms to the four caffeine oxidation pathways: An in vitro comparative study with cDNA-expressed P450s including CYP2C isoforms. Biochem. Pharmacol. 2008 , 76 , 543-551. [CrossRef]
- 10. Wojcikowski, J.; Daniel, W.A. Perazine at therapeutic drug concentrations inhibits human cytochrome P450 isoenzyme 1A2 (CYP1A2) and caffeine metabolism-An in vitro study. Pharmacol. Rep. 2009 , 61 , 851-858. [CrossRef]
- 11. Wojcikowski, J.; Danek, P.J.; Basinska-Ziobron, A.; Puklo, R.; Daniel, W.A. In vitro inhibition of human cytochrome P450 enzymes by the novel atypical antipsychotic drug asenapine: A prediction of possible drug-drug interactions. Pharmacol. Rep. 2020 , 72 , 612-621. [CrossRef]
- 12. Takahashi, E.; Fujita, K.; Kamataki, T.; Arimoto-Kobayashi, S.; Okamoto, K.; Negishi, T. Inhibition of human cytochrome P450 1B1, 1A1 and 1A2 by antigenotoxic compounds, purpurin and alizarin. Mutat. Res. 2002 , 508 , 147-156. [CrossRef]
- 13. Niwa, T.; Inoue-Yamamoto, S.; Shiraga, T.; Takagi, A. Effect of antifungal drugs on cytochrome P450 (CYP) 1A2, CYP2D6, and CYP2E1 activities in human liver microsomes. Biol. Pharm. Bull. 2005 , 28 , 1813-1816. [CrossRef]
- 14. Uehara, S.; Murayama, N.; Higuchi, Y.; Yoneda, N.; Yamazaki, H.; Suemizu, H. Comparison of mouse and human cytochrome P450 mediated-drug metabolising activities in hepatic and extrahepatic microsomes. Xenobiotica 2022 , 52 , 229-239. [CrossRef] [PubMed]
- 15. Burnham, E.A.; Abouda, A.A.; Bissada, J.E.; Nardone-White, D.T.; Beers, J.L.; Lee, J.; Vergne, M.J.; Jackson, K.D. Interindividual Variability in Cytochrome P450 3A and 1A Activity Influences Sunitinib Metabolism and Bioactivation. Chem. Res. Toxicol. 2022 , 35 , 792-806. [CrossRef]
- 16. Guo, J.; Zhu, X.; Badawy, S.; Ihsan, A.; Liu, Z.; Xie, C.; Wang, X. Metabolism and Mechanism of Human Cytochrome P450 Enzyme 1A2. Curr. Drug Metab. 2021 , 22 , 40-49. [CrossRef]
- 17. Lee, K.S.; Kim, S.K. Direct and metabolism-dependent cytochrome P450 inhibition assays for evaluating drug-drug interactions. J. Appl. Toxicol. 2013 , 33 , 100-108. [CrossRef] [PubMed]
- 18. Walsky, R.L.; Obach, R.S. Validated assays for human cytochrome P450 activities. Drug Metab. Dispos. 2004 , 32 , 647-660. [CrossRef]
- 19. McDonald, M.G.; Au, N.T.; Rettie, A.E. P450-Based Drug-Drug Interactions of Amiodarone and its Metabolites: Diversity of Inhibitory Mechanisms. Drug Metab. Dispos. 2015 , 43 , 1661-1669. [CrossRef] [PubMed]
- 20. Dinger, J.; Woods, C.; Brandt, S.D.; Meyer, M.R.; Maurer, H.H. Cytochrome P450 inhibition potential of new psychoactive substances of the tryptamine class. Toxicol. Lett. 2016 , 241 , 82-94. [CrossRef]
- 21. Shih, H.; Pickwell, G.V.; Guenette, D.K.; Bilir, B.; Quattrochi, L.C. Species differences in hepatocyte induction of CYP1A1 and CYP1A2 by omeprazole. Hum. Exp. Toxicol. 1999 , 18 , 95-105. [CrossRef]
- 22. Martinez, C.; Albet, C.; Agundez, J.A.; Herrero, E.; Carrillo, J.A.; Marquez, M.; Benitez, J.; Ortiz, J.A. Comparative in vitro and in vivo inhibition of cytochrome P450 CYP1A2, CYP2D6, and CYP3A by H2-receptor antagonists. Clin. Pharmacol. Ther. 1999 , 65 , 369-376. [CrossRef] [PubMed]
- 23. Sanderink, G.J.; Bournique, B.; Stevens, J.; Petry, M.; Martinet, M. Involvement of human CYP1A isoenzymes in the metabolism and drug interactions of riluzole in vitro. J. Pharmacol. Exp. Ther. 1997 , 282 , 1465-1472. [PubMed]
- 24. Weiss, J.; Sawa, E.; Riedel, K.D.; Haefeli, W.E.; Mikus, G. In vitro metabolism of the opioid tilidine and interaction of tilidine and nortilidine with CYP3A4, CYP2C19, and CYP2D6. Naunyn Schmiedebergs Arch. Pharmacol. 2008 , 378 , 275-282. [CrossRef] [PubMed]

- 25. Gallagher, E.P.; Wienkers, L.C.; Stapleton, P.L.; Kunze, K.L.; Eaton, D.L. Role of human microsomal and human complementary DNA-expressed cytochromes P4501A2 and P4503A4 in the bioactivation of aflatoxin B1. Cancer Res. 1994 , 54 , 101-108.
- 26. Granfors, M.T.; Backman, J.T.; Laitila, J.; Neuvonen, P.J. Tizanidine is mainly metabolized by cytochrome p450 1A2 in vitro. Br. J. Clin. Pharmacol. 2004 , 57 , 349-353. [CrossRef]
- 27. Juvonen, R.O.; Jokinen, E.M.; Javaid, A.; Lehtonen, M.; Raunio, H.; Pentikainen, O.T. Inhibition of human CYP1 enzymes by a classical inhibitor alpha-naphthoflavone and a novel inhibitor N-(3,5-dichlorophenyl)cyclopropanecarboxamide: An in vitro and in silico study. Chem. Biol. Drug Des. 2020 , 95 , 520-533. [CrossRef]
- 28. Reid, J.M.; Kuffel, M.J.; Miller, J.K.; Rios, R.; Ames, M.M. Metabolic activation of dacarbazine by human cytochromes P450: The role of CYP1A1, CYP1A2, and CYP2E1. Clin. Cancer Res. 1999 , 5 , 2192-2197.
- 29. Faucette, S.R.; Hawke, R.L.; Lecluyse, E.L.; Shord, S.S.; Yan, B.; Laethem, R.M.; Lindley, C.M. Validation of bupropion hydroxylation as a selective marker of human cytochrome P450 2B6 catalytic activity. Drug Metab. Dispos. 2000 , 28 , 1222-1230.
- 30. Desta, Z.; Saussele, T.; Ward, B.; Blievernicht, J.; Li, L.; Klein, K.; Flockhart, D.A.; Zanger, U.M. Impact of CYP2B6 polymorphism on hepatic efavirenz metabolism in vitro. Pharmacogenomics 2007 , 8 , 547-558. [CrossRef]
- 31. Nishiya, Y.; Hagihara, K.; Ito, T.; Tajima, M.; Miura, S.; Kurihara, A.; Farid, N.A.; Ikeda, T. Mechanism-based inhibition of human cytochrome P450 2B6 by ticlopidine, clopidogrel, and the thiolactone metabolite of prasugrel. Drug Metab. Dispos. 2009 , 37 , 589-593. [CrossRef] [PubMed]
- 32. Walsky, R.L.; Astuccio, A.V.; Obach, R.S. Evaluation of 227 drugs for in vitro inhibition of cytochrome P450 2B6. J. Clin. Pharmacol. 2006 , 46 , 1426-1438. [CrossRef] [PubMed]
- 33. Faucette, S.R.; Wang, H.; Hamilton, G.A.; Jolley, S.L.; Gilbert, D.; Lindley, C.; Yan, B.; Negishi, M.; LeCluyse, E.L. Regulation of CYP2B6 in primary human hepatocytes by prototypical inducers. Drug Metab. Dispos. 2004 , 32 , 348-358. [CrossRef] [PubMed]
- 34. Gerbal-Chaloin, S.; Daujat, M.; Pascussi, J.M.; Pichard-Garcia, L.; Vilarem, M.J.; Maurel, P. Transcriptional regulation of CYP2C9 gene. Role of glucocorticoid receptor and constitutive androstane receptor. J. Biol. Chem. 2002 , 277 , 209-217. [CrossRef]
- 35. Li, L.; Welch, M.A.; Li, Z.; Mackowiak, B.; Heyward, S.; Swaan, P.W.; Wang, H. Mechanistic Insights of Phenobarbital-Mediated Activation of Human but Not Mouse Pregnane X Receptor. Mol. Pharmacol. 2019 , 96 , 345-354. [CrossRef] [PubMed]
- 36. Madan, A.; Graham, R.A.; Carroll, K.M.; Mudra, D.R.; Burton, L.A.; Krueger, L.A.; Downey, A.D.; Czerwinski, M.; Forster, J.; Ribadeneira, M.D.; et al. Effects of prototypical microsomal enzyme inducers on cytochrome P450 expression in cultured human hepatocytes. Drug Metab. Dispos. 2003 , 31 , 421-431. [CrossRef] [PubMed]
- 37. Hesse, L.M.; Venkatakrishnan, K.; Court, M.H.; von Moltke, L.L.; Duan, S.X.; Shader, R.I.; Greenblatt, D.J. CYP2B6 mediates the in vitro hydroxylation of bupropion: Potential drug interactions with other antidepressants. Drug Metab. Dispos. 2000 , 28 , 1176-1183.
- 38. Turpeinen, M.; Nieminen, R.; Juntunen, T.; Taavitsainen, P.; Raunio, H.; Pelkonen, O. Selective inhibition of CYP2B6-catalyzed bupropion hydroxylation in human liver microsomes in vitro. Drug Metab. Dispos. 2004 , 32 , 626-631. [CrossRef]
- 39. Walsky, R.L.; Obach, R.S. A comparison of 2-phenyl-2-(1-piperidinyl)propane (ppp), 1,1 ' ,1 '' -phosphinothioylidynetrisaziridine (thioTEPA), clopidogrel, and ticlopidine as selective inactivators of human cytochrome P450 2B6. Drug Metab. Dispos. 2007 , 35 , 2053-2059. [CrossRef]
- 40. Lai, X.S.; Yang, L.P.; Li, X.T.; Liu, J.P.; Zhou, Z.W.; Zhou, S.F. Human CYP2C8: Structure, substrate specificity, inhibitor selectivity, inducers and polymorphisms. Curr. Drug Metab. 2009 , 10 , 1009-1047. [CrossRef]
- 41. Li, X.Q.; Bjorkman, A.; Andersson, T.B.; Ridderstrom, M.; Masimirembwa, C.M. Amodiaquine clearance and its metabolism to N-desethylamodiaquine is mediated by CYP2C8: A new high affinity and turnover enzyme-specific probe substrate. J. Pharmacol. Exp. Ther. 2002 , 300 , 399-407. [CrossRef]
- 42. Kim, M.J.; Lee, J.W.; Oh, K.S.; Choi, C.S.; Kim, K.H.; Han, W.S.; Yoon, C.N.; Chung, E.S.; Kim, D.H.; Shin, J.G. The tyrosine kinase inhibitor nilotinib selectively inhibits CYP2C8 activities in human liver microsomes. Drug Metab. Pharmacokinet. 2013 , 28 , 462-467. [CrossRef] [PubMed]
- 43. Wang, J.S.; Neuvonen, M.; Wen, X.; Backman, J.T.; Neuvonen, P.J. Gemfibrozil inhibits CYP2C8-mediated cerivastatin metabolism in human liver microsomes. Drug Metab. Dispos. 2002 , 30 , 1352-1356. [CrossRef]
- 44. Raucy, J.L.; Mueller, L.; Duan, K.; Allen, S.W.; Strom, S.; Lasker, J.M. Expression and induction of CYP2C P450 enzymes in primary cultures of human hepatocytes. J. Pharmacol. Exp. Ther. 2002 , 302 , 475-482. [CrossRef] [PubMed]
- 45. VandenBrink, B.M.; Foti, R.S.; Rock, D.A.; Wienkers, L.C.; Wahlstrom, J.L. Evaluation of CYP2C8 inhibition in vitro: Utility of montelukast as a selective CYP2C8 probe substrate. Drug Metab. Dispos. 2011 , 39 , 1546-1554. [CrossRef] [PubMed]
- 46. Polasek, T.M.; Elliot, D.J.; Lewis, B.C.; Miners, J.O. Mechanism-based inactivation of human cytochrome P4502C8 by drugs in vitro. J. Pharmacol. Exp. Ther. 2004 , 311 , 996-1007. [CrossRef]
- 47. Leemann, T.; Transon, C.; Dayer, P. Cytochrome P450TB (CYP2C): A major monooxygenase catalyzing diclofenac 4 ' -hydroxylation in human liver. Life Sci. 1993 , 52 , 29-34. [CrossRef]
- 48. Murayama, N.; Yajima, K.; Hikawa, M.; Shimura, K.; Ishii, Y.; Takada, M.; Uno, Y.; Utoh, M.; Iwasaki, K.; Yamazaki, H. Assessment of multiple cytochrome P450 activities in metabolically inactivated human liver microsomes and roles of P450 2C isoforms in reaction phenotyping studies. Biopharm. Drug Dispos. 2018 , 39 , 116-121. [CrossRef]
- 49. Mao, J.; Mohutsky, M.A.; Harrelson, J.P.; Wrighton, S.A.; Hall, S.D. Predictions of cytochrome P450-mediated drug-drug interactions using cryopreserved human hepatocytes: Comparison of plasma and protein-free media incubation conditions. Drug Metab. Dispos. 2012 , 40 , 706-716. [CrossRef]

- 50. Tang, C.; Shou, M.; Mei, Q.; Rushmore, T.H.; Rodrigues, A.D. Major role of human liver microsomal cytochrome P450 2C9 (CYP2C9) in the oxidative metabolism of celecoxib, a novel cyclooxygenase-II inhibitor. J. Pharmacol. Exp. Ther. 2000 , 293 , 453-459.
- 51. Giancarlo, G.M.; Venkatakrishnan, K.; Granda, B.W.; von Moltke, L.L.; Greenblatt, D.J. Relative contributions of CYP2C9 and 2C19 to phenytoin 4-hydroxylation in vitro: Inhibition by sulfaphenazole, omeprazole, and ticlopidine. Eur. J. Clin. Pharmacol. 2001 , 57 , 31-36. [CrossRef]
- 52. Chen, Y.; Ferguson, S.S.; Negishi, M.; Goldstein, J.A. Induction of human CYP2C9 by rifampicin, hyperforin, and phenobarbital is mediated by the pregnane X receptor. J. Pharmacol. Exp. Ther. 2004 , 308 , 495-501. [CrossRef] [PubMed]
- 53. Mori, K.; Hashimoto, H.; Takatsu, H.; Tsuda-Tsukimoto, M.; Kume, T. Cocktail-substrate assay system for mechanism-based inhibition of CYP2C9, CYP2D6, and CYP3A using human liver microsomes at an early stage of drug development. Xenobiotica 2009 , 39 , 415-422. [CrossRef]
- 54. Wrighton, S.A.; Stevens, J.C.; Becker, G.W.; VandenBranden, M. Isolation and characterization of human liver cytochrome P450 2C19: Correlation between 2C19 and S-mephenytoin 4 ' -hydroxylation. Arch. Biochem. Biophys. 1993 , 306 , 240-245. [CrossRef]
- 55. Suzuki, H.; Kneller, M.B.; Haining, R.L.; Trager, W.F.; Rettie, A.E. (+)-N-3-Benzyl-nirvanol and ( -)-N-3-benzyl-phenobarbital: New potent and selective in vitro inhibitors of CYP2C19. Drug Metab. Dispos. 2002 , 30 , 235-239. [CrossRef] [PubMed]
- 56. Ko, J.W.; Desta, Z.; Soukhova, N.V.; Tracy, T.; Flockhart, D.A. In vitro inhibition of the cytochrome P450 (CYP450) system by the antiplatelet drug ticlopidine: Potent effect on CYP2C19 and CYP2D6. Br. J. Clin. Pharmacol. 2000 , 49 , 343-351. [CrossRef]
- 57. Barecki, M.E.; Casciano, C.N.; Johnson, W.W.; Clement, R.P. In vitro characterization of the inhibition profile of loratadine, desloratadine, and 3-OH-desloratadine for five human cytochrome P-450 enzymes. Drug Metab. Dispos. 2001 , 29 , 1173-1175. [PubMed]
- 58. Khojasteh, S.C.; Prabhu, S.; Kenny, J.R.; Halladay, J.S.; Lu, A.Y. Chemical inhibitors of cytochrome P450 isoforms in human liver microsomes: A re-evaluation of P450 isoform selectivity. Eur. J. Drug Metab. Pharmacokinet. 2011 , 36 , 1-16. [CrossRef]
- 59. Reese, M.J.; Wurm, R.M.; Muir, K.T.; Generaux, G.T.; St John-Williams, L.; McConn, D.J. An in vitro mechanistic study to elucidate the desipramine/bupropion clinical drug-drug interaction. Drug Metab. Dispos. 2008 , 36 , 1198-1201. [CrossRef]
- 60. VandenBrink, B.M.; Foti, R.S.; Rock, D.A.; Wienkers, L.C.; Wahlstrom, J.L. Prediction of CYP2D6 drug interactions from in vitro data: Evidence for substrate-dependent inhibition. Drug Metab. Dispos. 2012 , 40 , 47-53. [CrossRef]
- 61. Bertelsen, K.M.; Venkatakrishnan, K.; Von Moltke, L.L.; Obach, R.S.; Greenblatt, D.J. Apparent mechanism-based inhibition of human CYP2D6 in vitro by paroxetine: Comparison with fluoxetine and quinidine. Drug Metab. Dispos. 2003 , 31 , 289-293. [CrossRef] [PubMed]

62.

Madeira, M.; Levine, M.; Chang, T.K.; Mirfazaelian, A.; Bellward, G.D. The effect of cimetidine on dextromethorphan O-

demethylase activity of human liver microsomes and recombinant CYP2D6.

Drug Metab. Dispos.

2004

,

32

, 460-467. [CrossRef]

- 63. Otton, S.V.; Ball, S.E.; Cheung, S.W.; Inaba, T.; Rudolph, R.L.; Sellers, E.M. Venlafaxine oxidation in vitro is catalysed by CYP2D6. Br. J. Clin. Pharmacol. 1996 , 41 , 149-156. [CrossRef] [PubMed]
- 64. Lee, J.; Fallon, J.K.; Smith, P.C.; Jackson, K.D. Formation of CYP3A-specific metabolites of ibrutinib in vitro is correlated with hepatic CYP3A activity and 4beta-hydroxycholesterol/cholesterol ratio. Clin. Transl. Sci. 2023 , 16 , 279-291. [CrossRef] [PubMed]
- 65. Walsky, R.L.; Obach, R.S.; Hyland, R.; Kang, P.; Zhou, S.; West, M.; Geoghegan, K.F.; Helal, C.J.; Walker, G.S.; Goosen, T.C.; et al. Selective mechanism-based inactivation of CYP3A4 by CYP3cide (PF-04981517) and its utility as an in vitro tool for delineating the relative roles of CYP3A4 versus CYP3A5 in the metabolism of drugs. Drug Metab. Dispos. 2012 , 40 , 1686-1697. [CrossRef] [PubMed]
- 66. Bissada, J.E.; Truong, V.; Abouda, A.A.; Wines, K.J.; Crouch, R.D.; Jackson, K.D. Interindividual Variation in CYP3A Activity Influences Lapatinib Bioactivation. Drug Metab. Dispos. 2019 , 47 , 1257-1269. [CrossRef]
- 67. Hellum, B.H.; Hu, Z.; Nilsen, O.G. The induction of CYP1A2, CYP2D6 and CYP3A4 by six trade herbal products in cultured primary human hepatocytes. Basic Clin. Pharmacol. Toxicol. 2007 , 100 , 23-30. [CrossRef]
- 68. Doran, A.C.; Burchett, W.; Landers, C.; Gualtieri, G.M.; Balesano, A.; Eng, H.; Dantonio, A.L.; Goosen, T.C.; Obach, R.S. Defining the Selectivity of Chemical Inhibitors Used for Cytochrome P450 Reaction Phenotyping: Overcoming Selectivity Limitations with a Six-Parameter Inhibition Curve-Fitting Approach. Drug Metab. Dispos. 2022 , 50 , 1259-1271. [CrossRef]
- 69. Zientek, M.A.; Youdim, K. Reaction phenotyping: Advances in the experimental strategies used to characterize the contribution of drug-metabolizing enzymes. Drug Metab. Dispos. 2015 , 43 , 163-181. [CrossRef]
- 70. Lu, A.Y.; Wang, R.W.; Lin, J.H. Cytochrome P450 in vitro reaction phenotyping: A re-evaluation of approaches used for P450 isoform identification. Drug Metab. Dispos. 2003 , 31 , 345-350. [CrossRef]
- 71. Rodrigues, A.D. Integrated cytochrome P450 reaction phenotyping: Attempting to bridge the gap between cDNA-expressed cytochromes P450 and native human liver microsomes. Biochem. Pharmacol. 1999 , 57 , 465-480. [CrossRef]
- 72. Zhang, H.; Davis, C.D.; Sinz, M.W.; Rodrigues, A.D. Cytochrome P450 reaction-phenotyping: An industrial perspective. Expert. Opin. Drug Metab. Toxicol. 2007 , 3 , 667-687. [CrossRef] [PubMed]
- 73. Dantonio, A.L.; Doran, A.C.; Obach, R.S. Intersystem Extrapolation Factors Are Substrate-Dependent for CYP3A4: Impact on Cytochrome P450 Reaction Phenotyping. Drug Metab. Dispos. 2022 , 50 , 249-257. [CrossRef]
- 74. Di, L. Reaction phenotyping to assess victim drug-drug interaction risks. Expert. Opin. Drug Discov. 2017 , 12 , 1105-1115. [CrossRef] [PubMed]

- 75. Doran, A.C.; Dantonio, A.L.; Gualtieri, G.M.; Balesano, A.; Landers, C.; Burchett, W.; Goosen, T.C.; Obach, R.S. An improved method for cytochrome p450 reaction phenotyping using a sequential qualitative-then-quantitative approach. Drug Metab. Dispos. 2022 , 50 , 1272-1286. [CrossRef] [PubMed]
- 76. Nagar, S.; Argikar, U.A.; Tweedie, D.J. Enzyme kinetics in drug metabolism: Fundamentals and applications. Methods Mol. Biol. 2014 , 1113 , 1-6. [CrossRef]
- 77. Zientek, M.A.; Goosen, T.C.; Tseng, E.; Lin, J.; Bauman, J.N.; Walker, G.S.; Kang, P.; Jiang, Y.; Freiwald, S.; Neul, D.; et al. In Vitro Kinetic Characterization of Axitinib Metabolism. Drug Metab. Dispos. 2016 , 44 , 102-114. [CrossRef]
- 78. Jones, H.M.; Houston, J.B. Substrate depletion approach for determining in vitro metabolic clearance: Time dependencies in hepatocyte and microsomal incubations. Drug Metab. Dispos. 2004 , 32 , 973-982. [CrossRef] [PubMed]
- 79. Rowland, M.; Matin, S.B. Kinetics of drug-drug interactions. J. Pharmacokinet. Biopharm. 1973 , 1 , 553-567. [CrossRef]
- 80. Bjornsson, T.D.; Callaghan, J.T.; Einolf, H.J.; Fischer, V.; Gan, L.; Grimm, S.; Kao, J.; King, S.P.; Miwa, G.; Ni, L.; et al. The conduct of in vitro and in vivo drug-drug interaction studies: A Pharmaceutical Research and Manufacturers of America (PhRMA) perspective. Drug Metab. Dispos. 2003 , 31 , 815-832. [CrossRef]
- 81. Bohnert, T.; Patel, A.; Templeton, I.; Chen, Y.; Lu, C.; Lai, G.; Leung, L.; Tse, S.; Einolf, H.J.; Wang, Y.H.; et al. Evaluation of a New Molecular Entity as a Victim of Metabolic Drug-Drug Interactions-An Industry Perspective. Drug Metab. Dispos. 2016 , 44 , 1399-1423. [CrossRef]
- 82. Drug Development and Drug Interactions|Table of Substrates, Inhibitors and Inducers. Available online: https://www.fda.gov/ drugs/drug-interactions-labeling/drug-development-and-drug-interactions-table-substrates-inhibitors-and-inducers (accessed on 19 October 2023).
- 83. Gelboin, H.V.; Krausz, K. Monoclonal antibodies and multifunctional cytochrome P450: Drug metabolism as paradigm. J. Clin. Pharmacol. 2006 , 46 , 353-372. [CrossRef]
- 84. Polsky-Fisher, S.L.; Cao, H.; Lu, P.; Gibson, C.R. Effect of cytochromes P450 chemical inhibitors and monoclonal antibodies on human liver microsomal esterase activity. Drug Metab. Dispos. 2006 , 34 , 1361-1366. [CrossRef]
- 85. Chen, Y.; Liu, L.; Nguyen, K.; Fretland, A.J. Utility of intersystem extrapolation factors in early reaction phenotyping and the quantitative extrapolation of human liver microsomal intrinsic clearance using recombinant cytochromes P450. Drug Metab. Dispos. 2011 , 39 , 373-382. [CrossRef] [PubMed]
- 86. Siu, Y.A.; Lai, W.G. Impact of Probe Substrate Selection on Cytochrome P450 Reaction Phenotyping Using the Relative Activity Factor. Drug Metab. Dispos. 2017 , 45 , 183-189. [CrossRef] [PubMed]
- 87. Obach, R.S. Linezolid Metabolism Is Catalyzed by Cytochrome P450 2J2, 4F2, and 1B1. Drug Metab. Dispos. 2022 , 50 , 413-421. [CrossRef]
- 88. Wynalda, M.A.; Hauer, M.J.; Wienkers, L.C. Oxidation of the novel oxazolidinone antibiotic linezolid in human liver microsomes. Drug Metab. Dispos. 2000 , 28 , 1014-1017. [PubMed]
- 89. Watanabe, R.; Kawata, T.; Ueda, S.; Shinbo, T.; Higashimori, M.; Natsume-Kitatani, Y.; Mizuguchi, K. Prediction of the Contribution Ratio of a Target Metabolic Enzyme to Clearance from Chemical Structure Information. Mol. Pharm. 2023 , 20 , 419-426. [CrossRef]
- 90. Keefer, C.E.; Chang, G.; Di, L.; Woody, N.A.; Tess, D.A.; Osgood, S.M.; Kapinos, B.; Racich, J.; Carlo, A.A.; Balesano, A.; et al. The Comparison of Machine Learning and Mechanistic In Vitro-In Vivo Extrapolation Models for the Prediction of Human Intrinsic Clearance. Mol. Pharm. 2023 , 20 , 5616-5630. [CrossRef]
- 91. Youdim, K.A.; Zayed, A.; Dickins, M.; Phipps, A.; Griffiths, M.; Darekar, A.; Hyland, R.; Fahmi, O.; Hurst, S.; Plowchalk, D.R.; et al. Application of CYP3A4 in vitro data to predict clinical drug-drug interactions; predictions of compounds as objects of interaction. Br. J. Clin. Pharmacol. 2008 , 65 , 680-692. [CrossRef]
- 92. Eagling, V.A.; Tjia, J.F.; Back, D.J. Differential selectivity of cytochrome P450 inhibitors against probe substrates in human and rat liver microsomes. Br. J. Clin. Pharmacol. 1998 , 45 , 107-114. [CrossRef]
- 93. Nirogi, R.; Palacharla, R.C.; Uthukam, V.; Manoharan, A.; Srikakolapu, S.R.; Kalaikadhiban, I.; Boggavarapu, R.K.; Ponnamaneni, R.K.; Ajjala, D.R.; Bhyrapuneni, G. Chemical inhibitors of CYP450 enzymes in liver microsomes: Combining selectivity and unbound fractions to guide selection of appropriate concentration in phenotyping assays. Xenobiotica 2015 , 45 , 95-106. [CrossRef] [PubMed]
- 94. Pearce, R.E.; McIntyre, C.J.; Madan, A.; Sanzgiri, U.; Draper, A.J.; Bullock, P.L.; Cook, D.C.; Burton, L.A.; Latham, J.; Nevins, C.; et al. Effects of freezing, thawing, and storing human liver microsomes on cytochrome P450 activity. Arch. Biochem. Biophys. 1996 , 331 , 145-169. [CrossRef]
- 95. Elaut, G.; Papeleu, P.; Vinken, M.; Henkens, T.; Snykers, S.; Vanhaecke, T.; Rogiers, V. Hepatocytes in suspension. Methods Mol. Biol. 2006 , 320 , 255-263. [CrossRef] [PubMed]
- 96. Stringer, R.; Nicklin, P.L.; Houston, J.B. Reliability of human cryopreserved hepatocytes and liver microsomes as in vitro systems to predict metabolic clearance. Xenobiotica 2008 , 38 , 1313-1329. [CrossRef]
- 97. Chan, T.S.; Yu, H.; Moore, A.; Khetani, S.R.; Tweedie, D. Meeting the Challenge of Predicting Hepatic Clearance of Compounds Slowly Metabolized by Cytochrome P450 Using a Novel Hepatocyte Model, HepatoPac. Drug Metab. Dispos. 2019 , 47 , 58-66. [CrossRef]
- 98. Klammers, F.; Goetschi, A.; Ekiciler, A.; Walter, I.; Parrott, N.; Fowler, S.; Umehara, K. Estimation of Fraction Metabolized by Cytochrome P450 Enzymes Using Long-Term Cocultured Human Hepatocytes. Drug Metab. Dispos. 2022 , 50 , 566-575. [CrossRef] [PubMed]

- 99. Lu, A.Y. Liver microsomal drug-metabolizing enzyme system: Functional components and their properties. Fed. Proc. 1976 , 35 , 2460-2463.
- 100. Asha, S.; Vidyavathi, M. Role of human liver microsomes in in vitro metabolism of drugs-A review. Appl. Biochem. Biotechnol. 2010 , 160 , 1699-1722. [CrossRef]
- 101. Cerny, M.A. Prevalence of Non-Cytochrome P450-Mediated Metabolism in Food and Drug Administration-Approved Oral and Intravenous Drugs: 2006-2015. Drug Metab. Dispos. 2016 , 44 , 1246-1252. [CrossRef]
- 102. Ring, B.; Wrighton, S.A.; Mohutsky, M. Reversible mechanisms of enzyme inhibition and resulting clinical significance. Methods Mol. Biol. 2014 , 1113 , 37-56. [CrossRef]
- 103. Lin, J.H.; Lu, A.Y. Inhibition and induction of cytochrome P450 and the clinical implications. Clin. Pharmacokinet. 1998 , 35 , 361-390. [CrossRef] [PubMed]
- 104. Seibert, E.; Tracy, T.S. Fundamentals of enzyme kinetics. Methods Mol. Biol. 2014 , 1113 , 9-22. [CrossRef] [PubMed]
- 105. Vieira, M.L.; Kirby, B.; Ragueneau-Majlessi, I.; Galetin, A.; Chien, J.Y.; Einolf, H.J.; Fahmi, O.A.; Fischer, V.; Fretland, A.; Grime, K.; et al. Evaluation of various static in vitro-in vivo extrapolation models for risk assessment of the CYP3A inhibition potential of an investigational drug. Clin. Pharmacol. Ther. 2014 , 95 , 189-198. [CrossRef] [PubMed]
- 106. Grimm, S.W.; Einolf, H.J.; Hall, S.D.; He, K.; Lim, H.K.; Ling, K.H.; Lu, C.; Nomeir, A.A.; Seibert, E.; Skordos, K.W.; et al. The conduct of in vitro studies to address time-dependent inhibition of drug-metabolizing enzymes: A perspective of the pharmaceutical research and manufacturers of America. Drug Metab. Dispos. 2009 , 37 , 1355-1370. [CrossRef] [PubMed]
- 107. Riley, R.J.; Grime, K.; Weaver, R. Time-dependent CYP inhibition. Expert. Opin. Drug Metab. Toxicol. 2007 , 3 , 51-66. [CrossRef] [PubMed]
- 108. Levine, M.; Bellward, G.D. Effect of cimetidine on hepatic cytochrome P450: Evidence for formation of a metabolite-intermediate complex. Drug Metab. Dispos. 1995 , 23 , 1407-1411. [PubMed]
- 109. Takakusa, H.; Wahlin, M.D.; Zhao, C.; Hanson, K.L.; New, L.S.; Chan, E.C.; Nelson, S.D. Metabolic intermediate complex formation of human cytochrome P450 3A4 by lapatinib. Drug Metab. Dispos. 2011 , 39 , 1022-1030. [CrossRef] [PubMed]
- 110. Watanabe, A.; Nakamura, K.; Okudaira, N.; Okazaki, O.; Sudo, K. Risk assessment for drug-drug interaction caused by metabolism-based inhibition of CYP3A using automated in vitro assay systems and its application in the early drug discovery process. Drug Metab. Dispos. 2007 , 35 , 1232-1238. [CrossRef]
- 111. Hollenberg, P.F.; Kent, U.M.; Bumpus, N.N. Mechanism-based inactivation of human cytochromes p450s: Experimental characterization, reactive intermediates, and clinical implications. Chem. Res. Toxicol. 2008 , 21 , 189-205. [CrossRef]
- 112. Bandyopadhyay, A.; Gao, J. Targeting biomolecules with reversible covalent chemistry. Curr. Opin. Chem. Biol. 2016 , 34 , 110-116. [CrossRef]
- 113. Silverman, R.B. Mechanism-based enzyme inactivators. Methods Enzymol. 1995 , 249 , 240-283. [CrossRef] [PubMed]
- 114. Imai, H.; Kotegawa, T.; Ohashi, K. Duration of drug interactions: Putative time courses after mechanism-based inhibition or induction of CYPs. Expert. Rev. Clin. Pharmacol. 2011 , 4 , 409-411. [CrossRef]
- 115. Mohutsky, M.; Hall, S.D. Irreversible enzyme inhibition kinetics and drug-drug interactions. Methods Mol. Biol. 2014 , 1113 , 57-91. [CrossRef] [PubMed]
- 116. Zlokarnik, G.; Grootenhuis, P.D.; Watson, J.B. High throughput P450 inhibition screens in early drug discovery. Drug Discov. Today 2005 , 10 , 1443-1450. [CrossRef]
- 117. Fowler, S.; Zhang, H. In vitro evaluation of reversible and irreversible cytochrome P450 inhibition: Current status on methodologies and their utility for predicting drug-drug interactions. AAPS J. 2008 , 10 , 410-424. [CrossRef] [PubMed]
- 118. Crespi, C.L.; Miller, V.P.; Stresser, D.M. Design and application of fluorometric assays for human cytochrome P450 inhibition. Methods Enzymol. 2002 , 357 , 276-284. [CrossRef]
- 119. Obach, R.S.L.K. Drug interaction studies in the drug development process: Studies in vitro. In Handbook of Drug Metabolism ; Paul, G., Pearson, L.C.W., Eds.; CRC Press: Boca Raton, FL, USA, 2019; pp. 429-466.
- 120. Berger, B.; Donzelli, M.; Maseneni, S.; Boess, F.; Roth, A.; Krahenbuhl, S.; Haschke, M. Comparison of Liver Cell Models Using the Basel Phenotyping Cocktail. Front. Pharmacol. 2016 , 7 , 443. [CrossRef]
- 121. Rodrigues, A.D.; Kukulka, M.J.; Surber, B.W.; Thomas, S.B.; Uchic, J.T.; Rotert, G.A.; Michel, G.; Thome-Kromer, B.; Machinist, J.M. Measurement of liver microsomal cytochrome p450 (CYP2D6) activity using [O-methyl-14C]dextromethorphan. Anal. Biochem. 1994 , 219 , 309-320. [CrossRef]
- 122. Mikov, M.; Danic, M.; Pavlovic, N.; Stanimirov, B.; Golocorbin-Kon, S.; Stankov, K.; Al-Salami, H. The Role of Drug Metabolites in the Inhibition of Cytochrome P450 Enzymes. Eur. J. Drug Metab. Pharmacokinet. 2017 , 42 , 881-890. [CrossRef]
- 123. Tang, W.; Wang, R.W.; Lu, A.Y. Utility of recombinant cytochrome p450 enzymes: A drug metabolism perspective. Curr. Drug Metab. 2005 , 6 , 503-517. [CrossRef]
- 124. Wright, W.C.; Chenge, J.; Chen, T. Structural Perspectives of the CYP3A Family and Their Small Molecule Modulators in Drug Metabolism. Liver Res. 2019 , 3 , 132-142. [CrossRef] [PubMed]
- 125. Kato, H. Computational prediction of cytochrome P450 inhibition and induction. Drug Metab. Pharmacokinet. 2020 , 35 , 30-44. [CrossRef] [PubMed]
- 126. Plonka, W.; Stork, C.; Sicho, M.; Kirchmair, J. CYPlebrity: Machine learning models for the prediction of inhibitors of cytochrome P450 enzymes. Bioorg Med. Chem. 2021 , 46 , 116388. [CrossRef] [PubMed]

- 127. Racz, A.; Bajusz, D.; Miranda-Quintana, R.A.; Heberger, K. Machine learning models for classification tasks related to drug safety. Mol. Divers. 2021 , 25 , 1409-1424. [CrossRef] [PubMed]
- 128. Stoll, F.; Goller, A.H.; Hillisch, A. Utility of protein structures in overcoming ADMET-related issues of drug-like compounds. Drug Discov. Today 2011 , 16 , 530-538. [CrossRef]
- 129. Luo, G.; Guenthner, T.; Gan, L.S.; Humphreys, W.G. CYP3A4 induction by xenobiotics: Biochemistry, experimental methods and impact on drug discovery and development. Curr. Drug Metab. 2004 , 5 , 483-505. [CrossRef]
- 130. Niemi, M.; Backman, J.T.; Neuvonen, M.; Neuvonen, P.J.; Kivisto, K.T. Effects of rifampin on the pharmacokinetics and pharmacodynamics of glyburide and glipizide. Clin. Pharmacol. Ther. 2001 , 69 , 400-406. [CrossRef]
- 131. Niemi, M.; Kivisto, K.T.; Backman, J.T.; Neuvonen, P.J. Effect of rifampicin on the pharmacokinetics and pharmacodynamics of glimepiride. Br. J. Clin. Pharmacol. 2000 , 50 , 591-595. [CrossRef]
- 132. Lin, J.H. CYP induction-mediated drug interactions: In vitro assessment and clinical implications. Pharm. Res. 2006 , 23 , 1089-1116. [CrossRef]
- 133. Dickins, M. Induction of cytochromes P450. Curr. Top. Med. Chem. 2004 , 4 , 1745-1766. [CrossRef]
- 134. Pelkonen, O.; Turpeinen, M.; Hakkola, J.; Honkakoski, P.; Hukkanen, J.; Raunio, H. Inhibition and induction of human cytochrome P450 enzymes: Current status. Arch. Toxicol. 2008 , 82 , 667-715. [CrossRef] [PubMed]
- 135. Itkin, B.; Breen, A.; Turyanska, L.; Sandes, E.O.; Bradshaw, T.D.; Loaiza-Perez, A.I. New Treatments in Renal Cancer: The AhR Ligands. Int. J. Mol. Sci. 2020 , 21 , 3551. [CrossRef]
- 136. Schuetz, J.D.; Schuetz, E.G.; Thottassery, J.V.; Guzelian, P.S.; Strom, S.; Sun, D. Identification of a novel dexamethasone responsive enhancer in the human CYP3A5 gene and its activation in human and rat liver cells. Mol. Pharmacol. 1996 , 49 , 63-72. [PubMed]
- 137. Pascussi, J.M.; Drocourt, L.; Gerbal-Chaloin, S.; Fabre, J.M.; Maurel, P.; Vilarem, M.J. Dual effect of dexamethasone on CYP3A4 gene expression in human hepatocytes. Sequential role of glucocorticoid receptor and pregnane X receptor. Eur. J. Biochem. 2001 , 268 , 6346-6358. [CrossRef] [PubMed]
- 138. Chen, Y.; Zeng, L.; Wang, Y.; Tolleson, W.H.; Knox, B.; Chen, S.; Ren, Z.; Guo, L.; Mei, N.; Qian, F.; et al. The expression, induction and pharmacological activity of CYP1A2 are post-transcriptionally regulated by microRNA hsa-miR-132-5p. Biochem. Pharmacol. 2017 , 145 , 178-191. [CrossRef] [PubMed]
- 139. Carroccio, A.; Wu, D.; Cederbaum, A.I. Ethanol increases content and activity of human cytochrome P4502E1 in a transduced HepG2 cell line. Biochem. Biophys. Res. Commun. 1994 , 203 , 727-733. [CrossRef]
- 140. Zhang, S.Y.; Surapureddi, S.; Coulter, S.; Ferguson, S.S.; Goldstein, J.A. Human CYP2C8 is post-transcriptionally regulated by microRNAs 103 and 107 in human liver. Mol. Pharmacol. 2012 , 82 , 529-540. [CrossRef]
- 141. Li, D.; Tolleson, W.H.; Yu, D.; Chen, S.; Guo, L.; Xiao, W.; Tong, W.; Ning, B. Regulation of cytochrome P450 expression by microRNAs and long noncoding RNAs: Epigenetic mechanisms in environmental toxicology and carcinogenesis. J. Environ. Sci. Health C Environ. Carcinog. Ecotoxicol. Rev. 2019 , 37 , 180-214. [CrossRef]
- 142. Hakkola, J.; Hukkanen, J.; Turpeinen, M.; Pelkonen, O. Inhibition and induction of CYP enzymes in humans: An update. Arch. Toxicol. 2020 , 94 , 3671-3722. [CrossRef]
- 143. Dvorak, Z.; Pavek, P. Regulation of drug-metabolizing cytochrome P450 enzymes by glucocorticoids. Drug Metab. Rev. 2010 , 42 , 621-635. [CrossRef]
- 144. Nguyen, L.P.; Bradfield, C.A. The search for endogenous activators of the aryl hydrocarbon receptor. Chem. Res. Toxicol. 2008 , 21 , 102-116. [CrossRef] [PubMed]
- 145. Riddick, D.S. Fifty Years of Aryl Hydrocarbon Receptor Research as Reflected in the Pages of Drug Metabolism and Disposition. Drug Metab. Dispos. 2023 , 51 , 657-671. [CrossRef] [PubMed]
- 146. Kou, Z.; Dai, W. Aryl hydrocarbon receptor: Its roles in physiology. Biochem. Pharmacol. 2021 , 185 , 114428. [CrossRef]
- 147. Jin, U.H.; Lee, S.O.; Safe, S. Aryl hydrocarbon receptor (AHR)-active pharmaceuticals are selective AHR modulators in MDA-MB468 and BT474 breast cancer cells. J. Pharmacol. Exp. Ther. 2012 , 343 , 333-341. [CrossRef]
- 148. Dolwick, K.M.; Schmidt, J.V.; Carver, L.A.; Swanson, H.I.; Bradfield, C.A. Cloning and expression of a human Ah receptor cDNA. Mol. Pharmacol. 1993 , 44 , 911-917.
- 149. Bock, K.W. Aryl hydrocarbon receptor (AHR): From selected human target genes and crosstalk with transcription factors to multiple AHR functions. Biochem. Pharmacol. 2019 , 168 , 65-70. [CrossRef] [PubMed]
- 150. Arpiainen, S.; Raffalli-Mathieu, F.; Lang, M.A.; Pelkonen, O.; Hakkola, J. Regulation of the Cyp2a5 gene involves an aryl hydrocarbon receptor-dependent pathway. Mol. Pharmacol. 2005 , 67 , 1325-1333. [CrossRef] [PubMed]
- 151. Rivera, S.P.; Saarikoski, S.T.; Hankinson, O. Identification of a novel dioxin-inducible cytochrome P450. Mol. Pharmacol. 2002 , 61 , 255-259. [CrossRef]
- 152. Saarikoski, S.T.; Rivera, S.P.; Hankinson, O.; Husgafvel-Pursiainen, K. CYP2S1: A short review. Toxicol. Appl. Pharmacol. 2005 , 207 , 62-69. [CrossRef]
- 153. Watkins, R.E.; Wisely, G.B.; Moore, L.B.; Collins, J.L.; Lambert, M.H.; Williams, S.P.; Willson, T.M.; Kliewer, S.A.; Redinbo, M.R. The human nuclear xenobiotic receptor PXR: Structural determinants of directed promiscuity. Science 2001 , 292 , 2329-2333. [CrossRef]
- 154. Cheng, Y.; Redinbo, M.R. Activation of the human nuclear xenobiotic receptor PXR by the reverse transcriptase-targeted anti-HIV drug PNU-142721. Protein Sci. 2011 , 20 , 1713-1719. [CrossRef] [PubMed]

- 155. Buchman, C.D.; Chai, S.C.; Chen, T. A current structural perspective on PXR and CAR in drug metabolism. Expert. Opin. Drug Metab. Toxicol. 2018 , 14 , 635-647. [CrossRef] [PubMed]
- 156. Kliewer, S.A.; Goodwin, B.; Willson, T.M. The nuclear pregnane X receptor: A key regulator of xenobiotic metabolism. Endocr. Rev. 2002 , 23 , 687-702. [CrossRef] [PubMed]
- 157. Carnahan, V.E.; Redinbo, M.R. Structure and function of the human nuclear xenobiotic receptor PXR. Curr. Drug Metab. 2005 , 6 , 357-367. [CrossRef] [PubMed]
- 158. Jones, S.A.; Moore, L.B.; Shenk, J.L.; Wisely, G.B.; Hamilton, G.A.; McKee, D.D.; Tomkinson, N.C.; LeCluyse, E.L.; Lambert, M.H.; Willson, T.M.; et al. The pregnane X receptor: A promiscuous xenobiotic receptor that has diverged during evolution. Mol. Endocrinol. 2000 , 14 , 27-39. [CrossRef]
- 159. Moore, L.B.; Parks, D.J.; Jones, S.A.; Bledsoe, R.K.; Consler, T.G.; Stimmel, J.B.; Goodwin, B.; Liddle, C.; Blanchard, S.G.; Willson, T.M.; et al. Orphan nuclear receptors constitutive androstane receptor and pregnane X receptor share xenobiotic and steroid ligands. J. Biol. Chem. 2000 , 275 , 15122-15127. [CrossRef] [PubMed]
- 160. Lehmann, J.M.; McKee, D.D.; Watson, M.A.; Willson, T.M.; Moore, J.T.; Kliewer, S.A. The human orphan nuclear receptor PXR is activated by compounds that regulate CYP3A4 gene expression and cause drug interactions. J. Clin. Investig. 1998 , 102 , 1016-1023. [CrossRef]
- 161. Maglich, J.M.; Parks, D.J.; Moore, L.B.; Collins, J.L.; Goodwin, B.; Billin, A.N.; Stoltz, C.A.; Kliewer, S.A.; Lambert, M.H.; Willson, T.M.; et al. Identification of a novel human constitutive androstane receptor (CAR) agonist and its use in the identification of CAR target genes. J. Biol. Chem. 2003 , 278 , 17277-17283. [CrossRef]
- 162. Tzameli, I.; Pissios, P.; Schuetz, E.G.; Moore, D.D. The xenobiotic compound 1,4-bis[2-(3,5-dichloropyridyloxy)]benzene is an agonist ligand for the nuclear receptor CAR. Mol. Cell Biol. 2000 , 20 , 2951-2958. [CrossRef]
- 163. Henderson, C.J.; Kapelyukh, Y.; Scheer, N.; Rode, A.; McLaren, A.W.; MacLeod, A.K.; Lin, D.; Wright, J.; Stanley, L.A.; Wolf, C.R. An Extensively Humanized Mouse Model to Predict Pathways of Drug Disposition and Drug/Drug Interactions, and to Facilitate Design of Clinical Trials. Drug Metab. Dispos. 2019 , 47 , 601-615. [CrossRef]
- 164. Ma, X.; Cheung, C.; Krausz, K.W.; Shah, Y.M.; Wang, T.; Idle, J.R.; Gonzalez, F.J. A double transgenic mouse model expressing human pregnane X receptor and cytochrome P450 3A4. Drug Metab. Dispos. 2008 , 36 , 2506-2512. [CrossRef] [PubMed]
- 165. Ross, J.; Plummer, S.M.; Rode, A.; Scheer, N.; Bower, C.C.; Vogel, O.; Henderson, C.J.; Wolf, C.R.; Elcombe, C.R. Human constitutive androstane receptor (CAR) and pregnane X receptor (PXR) support the hypertrophic but not the hyperplastic response to the murine nongenotoxic hepatocarcinogens phenobarbital and chlordane in vivo. Toxicol. Sci. 2010 , 116 , 452-466. [CrossRef] [PubMed]
- 166. Scheer, N.; Kapelyukh, Y.; Rode, A.; Oswald, S.; Busch, D.; McLaughlin, L.A.; Lin, D.; Henderson, C.J.; Wolf, C.R. Defining Human Pathways of Drug Metabolism In Vivo through the Development of a Multiple Humanized Mouse Model. Drug Metab. Dispos. 2015 , 43 , 1679-1690. [CrossRef] [PubMed]
- 167. Nishimura, M.; Naito, S.; Yokoi, T. Tissue-specific mRNA expression profiles of human nuclear receptor subfamilies. Drug Metab. Pharmacokinet. 2004 , 19 , 135-149. [CrossRef] [PubMed]
- 168. Miki, Y.; Suzuki, T.; Tazawa, C.; Blumberg, B.; Sasano, H. Steroid and xenobiotic receptor (SXR), cytochrome P450 3A4 and multidrug resistance gene 1 in human adult and fetal tissues. Mol. Cell Endocrinol. 2005 , 231 , 75-85. [CrossRef] [PubMed]
- 169. Goodwin, B.; Redinbo, M.R.; Kliewer, S.A. Regulation of CYP3A gene transcription by the pregnane x receptor. Annu. Rev. Pharmacol. Toxicol. 2002 , 42 , 1-23. [CrossRef]
- 170. Klyushova, L.S.; Perepechaeva, M.L.; Grishanova, A.Y. The Role of CYP3A in Health and Disease. Biomedicines 2022 , 10 , 2686. [CrossRef]
- 171. Toriyabe, T.; Nagata, K.; Takada, T.; Aratsu, Y.; Matsubara, T.; Yoshinari, K.; Yamazoe, Y. Unveiling a new essential cis element for the transactivation of the CYP3A4 gene by xenobiotics. Mol. Pharmacol. 2009 , 75 , 677-684. [CrossRef]
- 172. Chen, S.; Wang, K.; Wan, Y.J. Retinoids activate RXR/CAR-mediated pathway and induce CYP3A. Biochem. Pharmacol. 2010 , 79 , 270-276. [CrossRef]
- 173. Timsit, Y.E.; Negishi, M. CAR and PXR: The xenobiotic-sensing receptors. Steroids 2007 , 72 , 231-246. [CrossRef]
- 174. Goodwin, B.; Moore, L.B.; Stoltz, C.M.; McKee, D.D.; Kliewer, S.A. Regulation of the human CYP2B6 gene by the nuclear pregnane X receptor. Mol. Pharmacol. 2001 , 60 , 427-431.
- 175. Moscovitz, J.E.; Kalgutkar, A.S.; Nulick, K.; Johnson, N.; Lin, Z.; Goosen, T.C.; Weng, Y. Establishing Transcriptional Signatures to Differentiate PXR-, CAR-, and AhR-Mediated Regulation of Drug Metabolism and Transport Genes in Cryopreserved Human Hepatocytes. J. Pharmacol. Exp. Ther. 2018 , 365 , 262-271. [CrossRef]
- 176. Cho, D.Y.; Shen, J.H.; Lemler, S.M.; Skaar, T.C.; Li, L.; Blievernicht, J.; Zanger, U.M.; Kim, K.B.; Shin, J.G.; Flockhart, D.A.; et al. Rifampin enhances cytochrome P450 (CYP) 2B6-mediated efavirenz 8-hydroxylation in healthy volunteers. Drug Metab. Pharmacokinet. 2016 , 31 , 107-116. [CrossRef] [PubMed]
- 177. Fahmi, O.A.; Shebley, M.; Palamanda, J.; Sinz, M.W.; Ramsden, D.; Einolf, H.J.; Chen, L.; Wang, H. Evaluation of CYP2B6 Induction and Prediction of Clinical Drug-Drug Interactions: Considerations from the IQ Consortium Induction Working Group-An Industry Perspective. Drug Metab. Dispos. 2016 , 44 , 1720-1730. [CrossRef] [PubMed]
- 178. Rasmussen, M.K.; Daujat-Chavanieu, M.; Gerbal-Chaloin, S. Activation of the aryl hydrocarbon receptor decreases rifampicininduced CYP3A4 expression in primary human hepatocytes and HepaRG. Toxicol. Lett. 2017 , 277 , 1-8. [CrossRef]

- 179. Luo, G.; Cunningham, M.; Kim, S.; Burn, T.; Lin, J.; Sinz, M.; Hamilton, G.; Rizzo, C.; Jolley, S.; Gilbert, D.; et al. CYP3A4 induction by drugs: Correlation between a pregnane X receptor reporter gene assay and CYP3A4 expression in human hepatocytes. Drug Metab. Dispos. 2002 , 30 , 795-804. [CrossRef]
- 180. Luo, G.; Lin, J.; Fiske, W.D.; Dai, R.; Yang, T.J.; Kim, S.; Sinz, M.; LeCluyse, E.; Solon, E.; Brennan, J.M.; et al. Concurrent induction and mechanism-based inactivation of CYP3A4 by an L-valinamide derivative. Drug Metab. Dispos. 2003 , 31 , 1170-1175. [CrossRef] [PubMed]
- 181. Tsutsui, H.; Kuramoto, S.; Ozeki, K. Evaluation of Methods to Assess CYP3A Induction Risk in Clinical Practice Using in Vitro Induction Parameters. Biol. Pharm. Bull. 2021 , 44 , 338-349. [CrossRef]
- 182. Yoshida, K.; Zhao, P.; Zhang, L.; Abernethy, D.R.; Rekic, D.; Reynolds, K.S.; Galetin, A.; Huang, S.M. In Vitro-In Vivo Extrapolation of Metabolism- and Transporter-Mediated Drug-Drug Interactions-Overview of Basic Prediction Methods. J. Pharm. Sci. 2017 , 106 , 2209-2213. [CrossRef]
- 183. Jones, B.C.; Rollison, H.; Johansson, S.; Kanebratt, K.P.; Lambert, C.; Vishwanathan, K.; Andersson, T.B. Managing the Risk of CYP3A Induction in Drug Development: A Strategic Approach. Drug Metab. Dispos. 2017 , 45 , 35-41. [CrossRef]
- 184. Soldatow, V.Y.; Lecluyse, E.L.; Griffith, L.G.; Rusyn, I. In vitro models for liver toxicity testing. Toxicol. Res. 2013 , 2 , 23-39. [CrossRef] [PubMed]
- 185. den Braver-Sewradj, S.P.; den Braver, M.W.; Vermeulen, N.P.; Commandeur, J.N.; Richert, L.; Vos, J.C. Inter-donor variability of phase I/phase II metabolism of three reference drugs in cryopreserved primary human hepatocytes in suspension and monolayer. Toxicol. Vitr. 2016 , 33 , 71-79. [CrossRef] [PubMed]
- 186. Bell, C.C.; Dankers, A.C.A.; Lauschke, V.M.; Sison-Young, R.; Jenkins, R.; Rowe, C.; Goldring, C.E.; Park, K.; Regan, S.L.; Walker, T.; et al. Comparison of Hepatic 2D Sandwich Cultures and 3D Spheroids for Long-term Toxicity Applications: A Multicenter Study. Toxicol. Sci. 2018 , 162 , 655-666. [CrossRef] [PubMed]
- 187. Rowe, C.; Gerrard, D.T.; Jenkins, R.; Berry, A.; Durkin, K.; Sundstrom, L.; Goldring, C.E.; Park, B.K.; Kitteringham, N.R.; Hanley, K.P.; et al. Proteome-wide analyses of human hepatocytes during differentiation and dedifferentiation. Hepatology 2013 , 58 , 799-809. [CrossRef] [PubMed]
- 188. Bell, C.C.; Hendriks, D.F.; Moro, S.M.; Ellis, E.; Walsh, J.; Renblom, A.; Fredriksson Puigvert, L.; Dankers, A.C.; Jacobs, F.; Snoeys, J.; et al. Characterization of primary human hepatocyte spheroids as a model system for drug-induced liver injury, liver function and disease. Sci. Rep. 2016 , 6 , 25187. [CrossRef] [PubMed]
- 189. Jarvinen, E.; Hammer, H.S.; Potz, O.; Ingelman-Sundberg, M.; Stage, T.B. 3D Spheroid Primary Human Hepatocytes for Prediction of Cytochrome P450 and Drug Transporter Induction. Clin. Pharmacol. Ther. 2023 , 113 , 1284-1294. [CrossRef]
- 190. Mills, J.B.; Rose, K.A.; Sadagopan, N.; Sahi, J.; de Morais, S.M. Induction of drug metabolism enzymes and MDR1 using a novel human hepatocyte cell line. J. Pharmacol. Exp. Ther. 2004 , 309 , 303-309. [CrossRef] [PubMed]
- 191. Ripp, S.L.; Mills, J.B.; Fahmi, O.A.; Trevena, K.A.; Liras, J.L.; Maurer, T.S.; de Morais, S.M. Use of immortalized human hepatocytes to predict the magnitude of clinical drug-drug interactions caused by CYP3A4 induction. Drug Metab. Dispos. 2006 , 34 , 1742-1748. [CrossRef]
- 192. Hariparsad, N.; Carr, B.A.; Evers, R.; Chu, X. Comparison of immortalized Fa2N-4 cells and human hepatocytes as in vitro models for cytochrome P450 induction. Drug Metab. Dispos. 2008 , 36 , 1046-1055. [CrossRef]
- 193. Aninat, C.; Piton, A.; Glaise, D.; Le Charpentier, T.; Langouet, S.; Morel, F.; Guguen-Guillouzo, C.; Guillouzo, A. Expression of cytochromes P450, conjugating enzymes and nuclear receptors in human hepatoma HepaRG cells. Drug Metab. Dispos. 2006 , 34 , 75-83. [CrossRef]
- 194. Antherieu, S.; Chesne, C.; Li, R.; Camus, S.; Lahoz, A.; Picazo, L.; Turpeinen, M.; Tolonen, A.; Uusitalo, J.; Guguen-Guillouzo, C.; et al. Stable expression, activity, and inducibility of cytochromes P450 in differentiated HepaRG cells. Drug Metab. Dispos. 2010 , 38 , 516-525. [CrossRef]
- 195. Kanebratt, K.P.; Andersson, T.B. HepaRG cells as an in vitro model for evaluation of cytochrome P450 induction in humans. Drug Metab. Dispos. 2008 , 36 , 137-145. [CrossRef] [PubMed]
- 196. McGinnity, D.F.; Zhang, G.; Kenny, J.R.; Hamilton, G.A.; Otmani, S.; Stams, K.R.; Haney, S.; Brassil, P.; Stresser, D.M.; Riley, R.J. Evaluation of multiple in vitro systems for assessment of CYP3A4 induction in drug discovery: Human hepatocytes, pregnane X receptor reporter gene, and Fa2N-4 and HepaRG cells. Drug Metab. Dispos. 2009 , 37 , 1259-1268. [CrossRef] [PubMed]
- 197. Grime, K.; Ferguson, D.D.; Riley, R.J. The use of HepaRG and human hepatocyte data in predicting CYP induction drug-drug interactions via static equation and dynamic mechanistic modelling approaches. Curr. Drug Metab. 2010 , 11 , 870-885. [CrossRef]
- 198. Kaneko, A.; Kato, M.; Sekiguchi, N.; Mitsui, T.; Takeda, K.; Aso, Y. In vitro model for the prediction of clinical CYP3A4 induction using HepaRG cells. Xenobiotica 2009 , 39 , 803-810. [CrossRef] [PubMed]
- 199. Guengerich, F.P. Human Cytochrome P450 Enzymes. In Cytochrome P450: Structure, Mechanism, and Biochemistry ; Ortiz de Montellano, P.R., Ed.; Springer International Publishing: Cham, Switzerland, 2015; pp. 523-785. [CrossRef]
- 200. Guengerich, F.P. Cytochrome P-450 3A4: Regulation and role in drug metabolism. Annu. Rev. Pharmacol. Toxicol. 1999 , 39 , 1-17. [CrossRef]
- 201. Ekroos, M.; Sjogren, T. Structural basis for ligand promiscuity in cytochrome P450 3A4. Proc. Natl. Acad. Sci. USA 2006 , 103 , 13682-13687. [CrossRef]
- 202. Wang, Y.M.; Ong, S.S.; Chai, S.C.; Chen, T. Role of CAR and PXR in xenobiotic sensing and metabolism. Expert. Opin. Drug Metab. Toxicol. 2012 , 8 , 803-817. [CrossRef]

- 203. Finch, C.K.; Chrisman, C.R.; Baciewicz, A.M.; Self, T.H. Rifampin and rifabutin drug interactions: An update. Arch. Intern. Med. 2002 , 162 , 985-992. [CrossRef]
- 204. Shirasaka, Y.; Chang, S.Y.; Grubb, M.F.; Peng, C.C.; Thummel, K.E.; Isoherranen, N.; Rodrigues, A.D. Effect of CYP3A5 expression on the inhibition of CYP3A-catalyzed drug metabolism: Impact on modeling CYP3A-mediated drug-drug interactions. Drug Metab. Dispos. 2013 , 41 , 1566-1574. [CrossRef]
- 205. Bellmann, R.; Smuszkiewicz, P. Pharmacokinetics of antifungal drugs: Practical implications for optimized treatment of patients. Infection 2017 , 45 , 737-779. [CrossRef] [PubMed]
- 206. Shou, M.; Grogan, J.; Mancewicz, J.A.; Krausz, K.W.; Gonzalez, F.J.; Gelboin, H.V.; Korzekwa, K.R. Activation of CYP3A4: Evidence for the simultaneous binding of two substrates in a cytochrome P450 active site. Biochemistry 1994 , 33 , 6450-6455. [CrossRef] [PubMed]
- 207. Hutzler, J.M.; Tracy, T.S. Atypical kinetic profiles in drug metabolism reactions. Drug Metab. Dispos. 2002 , 30 , 355-362. [CrossRef]

208. Leow, J.W.H.; Chan, E.C.Y. Atypical Michaelis-Menten kinetics in cytochrome P450 enzymes: A focus on substrate inhibition.

Biochem. Pharmacol.

2019

,

169

, 113615. [CrossRef]

Disclaimer/Publisher's Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.