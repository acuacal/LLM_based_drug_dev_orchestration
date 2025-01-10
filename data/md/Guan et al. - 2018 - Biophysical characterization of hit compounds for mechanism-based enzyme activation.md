<!-- image -->

<!-- image -->

<!-- image -->

Citation: Guan X, Upadhyay A, Munshi S, Chakrabarti R (2018) Biophysical characterization of hit compounds for mechanism-based enzyme activation. PLoS ONE 13(3): e0194175. https://doi. org/10.1371/journal.pone.0194175

Editor: Ivano Eberini, Universit à degli Studi di Milano, ITALY

Received:

November 21, 2017

Accepted:

February 26, 2018

Published: March 16, 2018

Copyright: © 2018 Guan et al. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Data Availability Statement: All relevant data are within the paper and its Supporting Information files.

Funding: The authors received no specific funding for this work.

Competing interests: The authors have declared that no competing interests exist.

## RESEARCHARTICLE

## Biophysical characterization of hit compounds for mechanism-based enzyme activation

Xiangying Guan ☯ , Alok Upadhyay ☯ , Sudipto Munshi, Raj Chakrabarti *

Division of Fundamental Research, Chakrabarti Advanced Technology, Mount Laurel, New Jersey, United States of America

- ☯ These authors contributed equally to this work.
- * raj@pmc-group.com

## Abstract

Across all families of enzymes, only a dozen or so distinct classes of non-natural small molecule activators have been characterized, with only four known modes of activation among them. All of these modes of activation rely on naturally evolved binding sites that trigger global conformational changes. Among the enzymes that are of greatest interest for small molecule activation are the seven sirtuin enzymes, nicotinamide adenine dinucleotide (NAD + )-dependent protein deacylases that play a central role in the regulation of healthspan and lifespan in organisms ranging from yeast to mammals. However, there is currently no understanding of how to design sirtuin-activating compounds beyond allosteric activators of SIRT1-catalyzed reactions that are limited to particular substrates. Here, we introduce a general mode of sirtuin activation that is distinct from the known modes of enzyme activation. Based on the conserved mechanism of sirtuin-catalyzed deacylation reactions, we establish biophysical properties of small molecule modulators that can in principle result in enzyme activation for diverse sirtuins and substrates. Building upon this framework, we propose strategies for the identification, characterization and evolution of hits for mechanismbased enzyme activating compounds.

## Introduction

The silent information regulator proteins (sirtuins) have emerged as critical regulators of many cellular pathways. In particular, these enzymes protect against age-related diseases and serve as key mediators of longevity in evolutionarily distant organismic models [1]. Sirtuins are NAD + -dependent lysine deacylases, requiring the cofactor NAD + to cleave acyl groups from lysine side chains of their substrate proteins, and producing nicotinamide (NAM) as a by-product. A thorough understanding of sirtuin chemistry is not only of fundamental importance, but also of considerable medicinal importance, since there is enormous interest in the development of new mechanism-based sirtuin modulators [2, 3]. The mechanism of sirtuincatalyzed deacylation is depicted in S1 Fig [4-9].

Recently, in order to extend mammalian healthspan and lifespan, intense interest has developed in the activation of the seven mammalian sirtuin enzymes (SIRT1-7). Prior work on

<!-- image -->

sirtuin activation has relied exclusively on experimental screening, with an emphasis on allosteric activation of the SIRT1 enzyme. Indeed, small molecule allosteric activators of SIRT1 have been demonstrated to induce lifespan extension in model organisms such as mice [10, 11]. Allosteric activation is one of four known modes by which small molecules can activate enzymes [12]. Allosteric activators most commonly function by decreasing the dissociation constant for the substrate (the acylated protein dissociation constant Kd , Ac -Pr in the case of sirtuins).

Nearly all known sirtuin activators allosterically target SIRT1, work with a limited set of substrates [13-18], and bind outside of the active site to an allosteric domain in SIRT1 that is not shared by SIRT2-7 [19]. It is now known that other sirtuins-including SIRT2, SIRT3 and SIRT6-and multiple protein substrates play significant roles in regulating mammalian longevity [20-22]. General strategies for the activation of any mammalian sirtuin (including activation of SIRT1 for other substrates) are hence of central importance, but not understood.

Foundations for the rational design of mechanism-based sirtuin activators have been lacking, partly due to the absence of a clear understanding of the kinetics of sirtuin-catalyzed deacylation. Several types of mechanism-based sirtuin inhibitors have been reported recently in the literature, including Ex-527 and Sir-Real2 [23-25]. However, mechanism-based activation has proven far more elusive, due to the difficulty in screening for the balance of properties needed for a modulator to have the net effect of accelerating catalytic turnover.

In this regard, unlike allosteric activators like resveratrol, which are SIRT1-specific and have not been successfully applied to other sirtuins [19], NAD + supplementation [26] can activate most mammalian sirtuins in a substrate-independent fashion. The effects of NAD + supplementation are not specific to sirtuins and prohibitively high concentrations of NAD + , along with associated undesirable side effects, may be required to elicit the increases in sirtuin activity required to combat age-related diseases. A preferred general strategy for activation of sirtuins (S1 Fig) would be to lower the Km for NAD + ( Km , NAD + ). Km , NAD + reduction would have a similar activating effect to NAD + supplementation, but would be selective for sirtuins and could potentially even provide isoform specific sirtuin activation. Importantly, due to the sirtuin nicotinamide cleavage reaction that involves the NAD + cofactor, modulation of Km , NAD + may in principle be achievable by means other than altering the binding affinity of NAD + . Unlike allosteric activation that reduces Kd , Ac -Pr , this approach could be applicable to multiple sirtuins and substrates.

Several compounds have been reported in the literature as being activators of sirtuins other than SIRT1 [27-30]. However, some of the aforementioned compounds have not been characterized using initial rate assays [27, 29] and others have been studied using only labeled activity assays [29] that may be susceptible to false positives. Very little is known about the mechanistic functioning of these activators. However, such an understanding is critical to the rational design of mechanism-based activators.

In this paper, we present a general framework for activation of sirtuin enzymes that is distinct from any of the known modes of enzyme activation. We first introduce a steady-state model of sirtuin-catalyzed deacylation reactions in the presence of NAD + cofactor and endogenous inhibitor NAM, and then establish quantitatively how k cat /Km , NAD+ can be modified by small molecules, identifying the biophysical properties that small molecules must have to function as such mechanism-based activators. The principles introduced can also be generalized to the reduction of peptide substrate Km through non-allosteric mechanisms. We propose strategies suitable for designing mechanism-based sirtuin activating compounds (MB-STACs), and describe how to characterize sirtuin modulators in order to determine whether they possess the proposed characteristics of MB-STACs presented.

<!-- image -->

## Results

## Steady-state sirtuin kinetic modeling

To a greater extent than inhibitor design, rational activator design requires the use of a mechanistic model in the workflow. In this section we develop a steady state model for sirtuin-catalyzed deacylation that is suitable for a) investigation of the mode of action of mechanismbased sirtuin modulators, including activators; b) design of MB-STACs. We first summarize the state of knowledge regarding the sirtuin-catalyzed deacylation mechanism.

The sirtuin catalytic cycle (S1 Fig) is believed to proceed in two consecutive stages [4]. The initial stage (ADP-ribosylation) involves the cleavage of the NAM moiety of NAD + and the nucleophilic attack of the acyl-Lys side chain of the protein substrate to form a positively charged O-alkylimidate intermediate [4, 9]. NAM-induced reversal of the intermediate (the so-called base exchange reaction) causes reformation of NAD + and acyl-Lys protein. The energetics of this reversible reaction affects both the potency of NAM inhibition of sirtuins and the Michaelis constant for NAD + ( Km , NAD+ ). The second stage of sirtuin catalysis, which includes the rate-determining step, involves four successive steps that culminate in deacylation of the Lys side chain of the protein substrate and the formation of O-acetyl ADP ribose coproduct [4, 6, 31].

Atractable steady state model suitable for the purpose of mechanism-based sirtuin activator design must account for the following important features:

- · The calculated free energy of activation for NAM cleavage (ADP -ribosylation of the acylLys substrate) in the bacterial sirtuin enzyme Sir2Tm as computed through mixed quantum/ molecular mechanics (QM/MM) methods is 15.7 kcal mol -1 [5, 32]. An experimental value of 16.4 kcal mol -1 for the activation barrier in the yeast sirtuin homolog Hst2 was estimated from the reaction rate 6.7 s -1 of NAM formation. The NAM cleavage reaction is endothermic, with a computed Δ G of 4.98 kcal mol -1 in Sir2Tm [32].
- · The calculated free energy of activation for the rate limiting chemistry step (collapse of the bicyclic intermediate) from QM/MM simulations is 19.2 kcal mol -1 for Sir2Tm [33], in good agreement with the experimental value of 18.6 kcal mol -1 estimated from the k cat value of 0.170 ± 0.006 s -1 [34] (0.2 ± 0.03 s -1 for Hst2 [9]). We note that the relative magnitudes of the rate constants for the two slowest chemistry steps may vary for other sirtuins, like mammalian sirtuins. For some sirtuins, product release may be rate limiting.
- · The remaining steps in the catalytic cycle are significantly faster than the above steps. The other chemistry steps in stage 2 of the reaction are effectively irreversible [33], as is product release in the presence of saturating peptide concentrations.

Wehence include in our kinetic model representations of all steps in stage 1 of the reaction, including the NAM cleavage/base exchange and NAM binding steps. However, for simplicity, we do not include in the present model a representation of each of the individual chemistry steps in stage 2 of the reaction or final product release, instead subsuming these steps under the smallest rate constant, which we call k cat . Since all these steps are effectively irreversible, the full steady state model including these steps can be immediately derived from the basic model through simple modifications, to be described in a subsequent revision, that are not essential to the analysis of mechanism-based activation. The above observations motivate the kinetic model represented in S2 Fig [35]. S2 Fig shows a general reaction scheme for sirtuin deacylation including base exchange inhibition.

Because of the physiological benefits of improving catalytic efficiency under NAD + depletion rather than peptide depletion conditions, we assume saturating peptide conditions in our

<!-- image -->

kinetic modeling in this paper. However, precisely analogous equations could be derived for saturating NAD + , in the event that activation under peptide depletion conditions is desired. Wepreviously presented a preliminary theoretical and computational study of the mechanism by which NAM affects sirtuin activity [35]. In the present work, we build upon that foundation to establish a theoretical model for mechanism-based sirtuin modulators, including activators, in the presence of arbitrary concentrations of NAD + and NAM. The reaction mechanism of sirtuins precludes the use of rapid equilibrium methods for the derivation of even an approximate initial rate model; steady-state modeling is essential. The rate equations for the reaction network in S2 Fig enable the derivation of steady-state conditions for the reaction. Solving the linear system of algebraic steady-state equations and mass balance constraints for the concentrations [ E . Ac-Pr ], [ E . Ac-Pr . NAD + ], [ E . ADPR-Ac-Im . NAM ], [ E . ADPR-Ac-Im ], [ E . NAM ] in terms of the rate constants and [NAD + ], [NAM], which are assumed to be in significant excess and hence approximately equal to their initial concentrations [NAD + ] 0 , [NAM] 0 respectively, we obtain expressions of the form (1):

GLYPH<137> E : Ac GLYPH<0> Pr GLYPH<138> = GLYPH<137> E GLYPH<138> 0 GLYPH<136> c 11 GLYPH<135> c 12 GLYPH<137> NAM GLYPH<138> GLYPH<137> E : Ac GLYPH<0> Pr : NAD GLYPH<135> GLYPH<138> = GLYPH<137> E GLYPH<138> 0 GLYPH<136> c 21 GLYPH<137> NAD GLYPH<135> GLYPH<138> GLYPH<135> c 22 GLYPH<137> NAD GLYPH<135> GLYPH<138>GLYPH<137> NAM GLYPH<138> GLYPH<137> E : ADPR GLYPH<0> Ac GLYPH<0> Im : NAM GLYPH<138> = GLYPH<137> E GLYPH<138> 0 GLYPH<136> c 31 GLYPH<137> NAD GLYPH<135> GLYPH<138> GLYPH<135> c 32 GLYPH<137> NAD GLYPH<135> GLYPH<138>GLYPH<137> NAM GLYPH<138> GLYPH<137> E : ADPR GLYPH<0> Ac GLYPH<0> Im GLYPH<138> = GLYPH<137> E GLYPH<138> 0 GLYPH<136> c 41 GLYPH<137> NAD GLYPH<135> GLYPH<138> GLYPH<137> E : Ac GLYPH<0> Pr : NAM GLYPH<138> = GLYPH<137> E GLYPH<138> 0 GLYPH<136> c 51 GLYPH<137> NAD GLYPH<135> GLYPH<138> GLYPH<135> c 52 GLYPH<137> NAM GLYPH<138> GLYPH<135> c 53 GLYPH<137> NAD GLYPH<135> GLYPH<138>GLYPH<137> NAM GLYPH<138> GLYPH<135> c 54 GLYPH<137> NAM GLYPH<138> 2 GLYPH<133> 1 GLYPH<134>

where the term c 54 that is second order in [NAM] will be omitted from the analysis below. Expressions for the c ij 's are provided in the Appendix A2. The initial rate of deacylation can be then expressed

v v max GLYPH<136> GLYPH<137> NAD GLYPH<135> GLYPH<138> 1 GLYPH<135> GLYPH<137> NAM GLYPH<138> K 1 GLYPH<16> GLYPH<17> K m ; NAD GLYPH<135> 1 GLYPH<135> GLYPH<137> NAM GLYPH<138> K 2 GLYPH<16> GLYPH<17> GLYPH<135> GLYPH<137> NAD GLYPH<135> GLYPH<138> 1 GLYPH<135> GLYPH<137> NAM GLYPH<138> K 3 GLYPH<16> GLYPH<17> GLYPH<133> 2 GLYPH<134>

where the definitions of the steady state constants in terms of fundamental rate constants in the enzymatic reaction mechanism are presented in Appendix A1. Kex = k -2 /k 2 , and the approximations refer to the case where k4 << kj , j 6GLYPH<136> 4 . The quality of this approximation can be assessed for the chemistry steps based on QM/MM simulation data, which was cited above for yeast and bacterial sirtuins, or from experimental methods for the estimation of all rate constants in the model (see below). Expression (2) can be used to calculate the initial rate of sirtuin-catalyzed deacylation for specified intracellular concentrations of NAD + and NAM, assuming the rate constants are known.

Eq (2) is typically represented graphically in terms of either double reciprocal plots at constant [NAM] or Dixon plots at constant [NAD + ]. In the former case, the slope of the plot (1/v vs 1/ [NAD + ]) at [NAM] = 0 is K m ; NAD GLYPH<135> = v max , for which the expression is:

K m ; NAD GLYPH<135> v max GLYPH<136> 1 GLYPH<137> E GLYPH<138> 0 1 k 1 GLYPH<135> K d ; NAD GLYPH<135> k GLYPH<0> 3 GLYPH<135> k GLYPH<0> 2 k GLYPH<0> 3 k 2 GLYPH<18> GLYPH<19> GLYPH<136> K m ; NAD GLYPH<135> k cat GLYPH<137> E GLYPH<138> 0 GLYPH<133> 3 GLYPH<134>

whereas for the Dixon plot, the expression for the slope at 1/[NAD + ] = 0 is approximately [35, 36]:

1 K 3 1 v max GLYPH<25> 1 GLYPH<135> K ex K d ; NAM 1 k cat GLYPH<137> E GLYPH<138> 0 GLYPH<133> 4 GLYPH<134>

Wenote that Eq (3) for catalytic efficiency applies irrespective of the small k 4 approximation.

<!-- image -->

The steady state parameter α Eq (15) in Appendix A1, which is a measure of the extent of competitive inhibition by the endogenous inhibitor NAM against the cofactor NAD + , can be expressed in terms of the ratio of Kd , NAD+ and Km , NAD+ [35, 36]:

a GLYPH<136> K 3 K 2 GLYPH<25> K d ; NAD GLYPH<135> K m ; NAD GLYPH<135> K ex 1 GLYPH<135> K ex GLYPH<133> 5 GLYPH<134>

which, together with expression (12) in Appendix A1 for Km , NAD+ , demonstrates how the kinetics of inhibition of deacylation by NAM can reveal differences in NAD + binding affinity and NAM cleavage rates among sirtuins. In addition to the approximation k4 << kj , j 6GLYPH<136> 4 , several experimental observations can further simplify the form of the expressions for the sirtuin steady state constants. First, we assume k-3 >> kj , j 6GLYPH<136> -2 based on viscosity measurements that suggest NAM dissociates rapidly following cleavage [37]. Under this approximation, the expression for Km , NAD+ becomes:

K m ; NAD GLYPH<135> GLYPH<25> k 4 1 k 1 GLYPH<135> K d ; NAD GLYPH<135> k 2 GLYPH<18> GLYPH<19> GLYPH<133> 6 GLYPH<134>

Such approximations will be studied in greater detail in a subsequent work.

As can be seen from Fig 1B, the kinetics of the NAM cleavage reaction and the rate limiting step of deacylation both play essential roles in determining the value of Km , NAD+ . Note that in rapid equilibrium models of enzyme kinetics, which are not applicable to sirtuins, K m GLYPH<25> Kd . The difference between Kd , NAD+ and Km , NAD+ has important implications for mechanismbased activation of sirtuins by small molecules [35]. In particular, as we will show in this work, decrease of Km , NAD+ independently of Kd , NAD+ can increase the activity of sirtuins at [NAM] = 0. The kinetic model above establishes foundations for how this can be done.

## Mechanism-based sirtuin activation

Aprerequisite for enzyme activation is that the modulator must co-bind with substratesNAD + and acylated peptide in the case of sirtuins. Within the context of enzyme inhibition, two modes of action display this property: noncompetitive and uncompetitive inhibition. In the case of sirtuins, examples of noncompetitive inhibitors include SirReal2 [24], whereas examples of uncompetitive inhibitors include Ex-527 [23]. Though some known sirtuin inhibitors may satisfy the requirement of cobinding with substrates, they do not possess other critical attributes necessary for mechanism-based enzyme activation. While such compounds may have promising properties as potential hits for the development of mechanism-based activators, prior studies have only characterized their kinetic effects in terms of traditional rapid equilibrium formulations of enzyme inhibition, rather than a steady-state formulation for mechanism-based enzyme modulation. Although some previous work have begun to explore the mechanisms by which small molecules may activate sirtuins other than SIRT1 [38], further work aimed at establishing a foundation for the characterization and design of such compounds is needed.

Previous attempts to develop a general approach to sirtuin activation [37, 39] only considered competitive inhibitors of base exchange, which cannot activate in the absence of NAM. This is not actually a form of enzyme activation, but rather derepression of inhibition. Such derepression modalities based on competitive inhibition of product binding cannot be hits for activator design, since these compounds or their relatives cannot cobind with substrates. By contrast, here we present paradigms and design criteria for activation of sirtuins in either the absence or presence of NAM. Based on expression (3b) for Km , NAD+ , it is in principle possible to activate sirtuins (not just SIRT1) for any substrate by alteration of rate constants in the

<!-- image -->

Fig 1. General model for mechanism-based sirtuin enzyme activation. (A) The front face of the cube (blue) depicts the salient steps of the sirtuin reaction network in the absence of bound modulator. The back face of the cube (red) depicts the reaction network in the presence of bound modulator (denoted by 'A'). Each rate constant depicted on the front face has an associated modulated value on the back face, designated with a prime, which is a consequence of modulator binding. (B) The purple face is the apparent reaction network in the presence of a nonsaturating concentration of modulator.

<!-- image -->

https://doi.org/10.1371/journal.pone.0194175.g001

reaction mechanism other than k 1 , k -1 and k cat , so as to reduce Km , NAD+ , not only Kd , Ac-Pr as with allosteric activators, which increase the peptide binding affinity of SIRT1 in a substratedependent fashion. We now explore how this may be achieved by augmenting the kinetic model to include putative mechanism-based activators (A) that can bind simultaneously with NAD + and NAM. Fig 1 depicts the reaction diagram for mechanism-based activation of sirtuins. Note that only the top and front faces of this cube are relevant to the mechanism of action of the previously proposed competitive inhibitors of base exchange [37, 39]. Due to the novelty of the theoretical results on mechanism-based activation and their central role in the analysis that follows, the derivations of these results and associated approximations are provided.

Fig 2 displays the expressions for each of the modulated steady state constants in Appendix A1 according to the rapid equilibrium segments approximation. Note that

<!-- image -->

At any [A] there exist apparent values of each of the rate constants in the sirtuin reaction mechanism. These are denoted by 'app' in the Fig 1. There are also corresponding 'app' values of the steady state, Michaelis, and dissociation constants in Eq (3). Moreover, at saturating [A] of a known activator, the modulated equilibrium and dissociation constants (which do not depend on determination of steady state species concentrations) can be estimated with only deacylation experiments according to the theory presented above. The exchange equilibrium constant ( Kex ') and NAD + , NAM dissociation constants ( Kd , NAD + 0 and Kd , NAM 0 ) in the presence of A are related to their original values as follows:

K d ; NAD GLYPH<135> 0 GLYPH<136> K d ; NAD GLYPH<135> K d 2 ; A K d 1 ; A ; K ex 0 GLYPH<136> K ex K d 3 ; A K d 2 ; A ; K d ; NAM 0 GLYPH<136> K d ; NAM K d 3 ; A K d 4 ; A GLYPH<133> 7 GLYPH<134>

where the Kd , A 's are the dissociation constants for A depicted in Fig 1.

In order to predict the effect on K m ; NAD GLYPH<135> ; app of a modulator with specified relative binding affinities for the complexes in the sirtuin reaction mechanism, it is important to develop a model that is capable of quantifying, under suitable approximations, the effect of such a modulator on the apparent steady state parameters of the enzyme. Since the full steady state expression relating the original to the apparent rate constants has many terms containing products of additional side and back face rate constants, we use a rapid equilibrium segments approach to arrive at simple definitions of the apparent Michaelis constant and other steady state constants for the reaction in terms of the original expressions for these constants and the dissociation constants for binding of A to the various complexes in the sirtuin reaction mechanism. This provides a minimal model with the least number of additional parameters required to model sirtuin activation mechanisms. In our treatment, we will assume that rapid equilibrium applies on both the side faces and the back face. Under this approximation, at low [A] the expressions for the induced changes in each of the rate constant products appearing in the coefficients c ij and c i'j' , i' = i of (Eq 1) (see Appendix A2 for expressions for these products) are the same and linear in [A]. For example, in the case of E . Ac - Pr, the steady state species concentrations become:

GLYPH<137> E : Ac GLYPH<0> Pr GLYPH<138> = GLYPH<137> E : Ac GLYPH<0> Pr GLYPH<138> 0 GLYPH<25> c 11 GLYPH<135> c 12 GLYPH<137> NAM GLYPH<138> GLYPH<137> E : Ac GLYPH<0> Pr : A GLYPH<138> = GLYPH<137> E : Ac GLYPH<0> Pr GLYPH<138> 0 GLYPH<25> GLYPH<137> A GLYPH<138> K d 1 ; A GLYPH<133> c 11 GLYPH<135> c 12 GLYPH<137> NAM GLYPH<138>GLYPH<134> GLYPH<133> 8 GLYPH<134>

The rapid equilibrium segments expressions for all species concentrations in Eq (1) in the presence of A are provided in the S1 File. Expressions for apparent values of all steady state parameters introduced in Appendix A1 (i.e., modulated versions of constants v max , Km , NAD + , K 1 , K 2 , K 3 ) in the presence of a given [A] can now be derived. In the following, several types of approximations will be invoked:

- 1. rapid equilibrium segments approximation
- 2. k 4 GLYPH<133> 1 GLYPH<135> K dl ; A GLYPH<134> GLYPH<28> k j GLYPH<133> 1 GLYPH<135> K dl 0 ; A GLYPH<134> ; j 6GLYPH<136> 4 ; l GLYPH<136> 1 ; . . . ; 5
- 3. k GLYPH<0> 3 GLYPH<133> 1 GLYPH<135> K dl ; A GLYPH<134> GLYPH<29> k j GLYPH<133> 1 GLYPH<135> K dl 0 ; A GLYPH<134> ; j 6GLYPH<136> GLYPH<0> 3 ; l GLYPH<136> 1 ; . . . ; 5 (rapid NAM dissociation)

v max ; app GLYPH<137> E GLYPH<138> 0 GLYPH<136> k cat ; app GLYPH<136> GLYPH<133> c 31 ; app GLYPH<135> c 41 ; app GLYPH<134> c 21 ; app GLYPH<135> c 31 ; app GLYPH<135> c 41 ; app GLYPH<135> c 51 ; app GLYPH<25> k 4 c 41 GLYPH<133> 1 GLYPH<135> GLYPH<137> A GLYPH<138> = K dA ; 4 GLYPH<134> c 41 GLYPH<133> 1 GLYPH<135> GLYPH<137> A GLYPH<138> = K dA ; 4 GLYPH<134> GLYPH<136> k 4

Fig 2. Modulated expressions for the steady state constants in Appendix A1 according to the rapid equilibrium segments approximation. cij expressions are provided in the Appendix A2. In particular, we emphasize that assumption (ii) may not hold for several mammalian sirtuins, but we apply this approximation to simplify the equations and provide physical insight. The general equations without this approximation can readily be derived using the principles introduced.

<!-- image -->

[4] 1+ K [4] [4] [4] [4] 1+ 1+1+1+1 4 k, It[] Ka Ka

1+K

(1+[4]! Kasa ~ Ka

1

(I+[4]/

https://doi.org/10.1371/journal.pone.0194175.g002

<!-- image -->

remains roughly unchanged and is not listed in Fig 2 above since the primary goal of mechanism-based activation is to improve catalytic efficiency, which does not depends on vmax .

## Conditions for mechanism-based activation

Wenowconsider thermodynamic conditions on the binding of a modulator A for mechanism-based sirtuin activation under the rapid equilibrium segments approximation, along with the expected changes in the steady state, equilibrium and dissociation constants in the sirtuin reaction mechanism.

First, as noted above, vmax / [ E ] 0 is roughly unchanged within this family of mechanisms as long as the Kd , A 's for [A] binding to the various represented complexes in the reaction mechanism satisfy condition (iii). This is reasonable as long as the modulator does not lead to a significant increase in coproduct binding affinity and reduction in coproduct dissociation rate (for example, the stabilization of a closed loop conformation). As in the case of Ex-527 [23], the latter can render product dissociation rate limiting and reduce k cat . If k cat is reduced by the modulator, the net extent of activation will be reduced. However, even if this is the case, reduction in k cat will not affect catalytic efficiency k cat / Km . Hence it is justified to omit binding of A to the coproduct complex from the mechanism-based activation model. Moreover, binding of Awill not substantially reduce k cat if the rate limiting chemistry step is much slower than product release.

The goal of mechanism-based activation is to increase k cat,app / Km , app . According to Fig 2b, K m ; NAD GLYPH<135> ; app will be smaller than K m ; NAD GLYPH<135> if Kd 1, A / Kd 4, A GLYPH<21> ( Kd 1, A / Kd 2, A )( Kd 2, A / Kd 3, A )( Kd 3, A / Kd 4, A ) > 1.

To identify mechanisms by which this can occur in terms of the steps in the sirtuin-catalyzed reaction, we consider in turn each of these three respective ratios of Kd , A 's (or equivalently, the ΔΔ G 's of the NAD + binding, exchange, and NAM binding reactions as implied by Eq (7)) induced by A binding.

According to Fig 2e, K d1,A / K d2,A < 1 would imply that A binding increases the binding affinity of NAD + to the E.Ac-Pr complex. This is the primary means by which allosteric activators enhance activity, but not the only possibility for mechanism-based activation. In principle, it is possible for a mechanism-based activator to reduce Km , NAD+ even if K d1,A GLYPH<21> K d2,A . In this case, in order to have K m ; NAD GLYPH<135> ; app < K m ; NAD GLYPH<135> , we require ( Kd 2, A / Kd 3, A )( Kd 3, A / Kd 4, A ) > Kd 1, A / Kd 2, A or equivalently, according to (8), ( Kd , NAM 0 / Kex 0 )( Kex / Kd , NAM ) > Kd , NAD+ 0 / Kd , NAD+ . The decrease in K m ; NAD GLYPH<135> can then be due to modulation of the exchange rate constants that induces a decrease in Kex , an increase in Kd , NAM , or both. If Kd , NAM changes in the presence of modulator, this corresponds to mixed noncompetitive inhibition [35] of base exchange (Fig 1).

+

d 2 ; A K d 4 ; A for activators. Although the value of Kd 2 / Kd 4 required for activation is likely to be achieved primarily by altering the free energy change of the NAM cleavage reaction, our model accommodates the possibility of arbitrary combinations of ΔΔ Gex and ΔΔ Gbind , NAM .

As we have previously shown [35], the NAM moiety of NAD engages in nearly identical interactions with the enzyme before and after bond cleavage. The salient difference is a conformational change in a conserved phenylalanine side chain (e.g., Phe33 in Sir2Tm, Phe157 in SIRT3) that destabilizes NAM binding after bond cleavage [40, 41]. Since NAM binding is already destabilized by the native protein conformation in this way, and since under rapid NAMdissociation (approximation iii above, which is believed to hold for sirtuins [38]) k 2 and k -2 do not appear in the expression for Km , K d 2 ; A K d 3 ; A is likely to make the dominant contribution to K

In our original model for sirtuin kinetics in S2 Fig, we assumed that both Kd , NAM 'snamely, those for dissociation of NAM from E.Ac-Pr.NAM and E.ADPR-Pr-Im.NAM-are

<!-- image -->

roughly equal. We maintain this condition in the presence of A binding, which is reasonable given that A is assumed to not interact directly with the peptide or ADPR moiety. Hence, we have:

GLYPH<137> E : ADPR GLYPH<0> Pr GLYPH<0> Im GLYPH<138>GLYPH<137> NAM GLYPH<138> GLYPH<137> E : ADPR GLYPH<0> Pr GLYPH<0> Im : NAM GLYPH<138> GLYPH<25> GLYPH<137> E : Ac GLYPH<0> Pr GLYPH<138>GLYPH<137> NAM GLYPH<138> GLYPH<137> E : Ac GLYPH<0> Pr : NAM GLYPH<138> , K d 5 ; A GLYPH<25> K d 1 ; A K d 3 ; A K d 4 ; A GLYPH<133> 9 GLYPH<134>

Returning to the expression in Fig 2a for K m ; NAD GLYPH<135> ; app and substituting (1+[ A ]/ Kd 2, A )/(1+[ A ]/ Kd 1, A ) GLYPH<21> 1, the rapid equilibrium assumptions applied to the present system imply that in order to activate the enzyme at [NAM] = 0, if A does not improve cofactor binding affinity it must increase k 1 (k 1,app > k 1 ), k 2 (k 2,app > k 2 ) or both. The rapid equilibrium segments model is not able to distinguish between these scenarios. If A increases K d ; NAD GLYPH<135> ; app , it is unlikely that an increase k 1 will achieve activation. An increase in k 2 implies acceleration of the rate of NAM cleavage. In the rapid equilibrium segments framework, this occurs through preferential stabilization of the E.ADPR-Pr-Im complex. Note that across all sirtuins studied, NAM cleavage induces structural changes (for example, unwinding of a helical segment in the flexible cofactor binding loop [42, 43]) and such changes might enable preferential stabilization of the E. ADPR-Pr-Im complex, in a manner similar to the stabilization of specific loop conformations by mechanism-based inhibitors [23]. Indeed, stabilization of alternative, non-native conformations of this loop have been observed crystallographically by reported activators of sirtuins other than SIRT3, including both long-chain fatty acids [38, 44] and recently reported activators of SIRT5 and SIRT6 [30]. We discuss below the biophysical underpinnings whereby an increase in a forward rate constant could be achieved through preferential stabilization of the intermediate complex.

Given that an open loop conformation favors NAD + binding, if a closed loop conformation is stabilized by the modulator, we expect the following thermodynamic conditions on the binding of A to the various complexes in the sirtuin reaction mechanism:

K d 1 ; A GLYPH<20> K d 2 ; A ∃ K 0 d ; NAD GLYPH<135> GLYPH<21> K d ; NAD GLYPH<135> GLYPH<133> 10 GLYPH<134>

K d 2 ; A GLYPH<29> K d 3 ; A ∃ K 0 ex GLYPH<28> K ex

where the >> sign signifies that Kd 2, A / Kd 3, A > Kd 1, A / Kd 2, A . We also require the necessary but not sufficient condition that Kd 2, A / Kd 4, A > Kd 1, A / Kd 2, A . As noted above, increasing Kd 3, A / Kd 4, A (which would destabilize NAM binding) is not considered as a mode of activation since NAMis believed to already dissociate quickly from the native active sites of sirtuins. Within conventional nomenclature, decrease in Kex corresponds to hyperbolic (or partial) noncompetitive inhibition [35] of base exchange/activation of NAM cleavage (as opposed to complete quenching of the base exchange reaction; see Fig 1).

Wenow consider the effects of binding of such a modulator A that favors a closed cofactor loop conformation on the remaining steady state constants.

- · K 1, app : Reduction in K 1 , which is associated with a reduction in Kd 3, A / Kd 4, A (Fig 2d), can increase Km , NAD+ . A modulator has more favorable properties if K 1 does not decrease significantly, but as discussed above, an increase in K 1 will generally not be sufficiently for activation. Moreover, if K 3 increases in the presence of modulator, a decrease in K 1 may not be consequential.
- · K 2, app : With conditions (10), the expression in Fig 2c predicts a limited change in K 2 .

Fig 3 depicts the model-predicted changes to the various steady state, Michaelis and dissociation constants in the sirtuin reaction mechanism in the presence of such a modulator.

<!-- image -->

- · K 3, app : According to Fig 2b, in the presence of such a mechanism-based activator, K 3 is expected to increase by a factor more than that for K 2 under the rapid equilibrium segments approximation. This can occur due to an increase in Kd , NAM , a decrease in Kex , or both.
- · α app : According to the equations in Fig 2b and 2c, the aforementioned condition that Kd 2, A / Kd 4, A GLYPH<21> Kd 1, A / Kd 2, A implies an increase in α .

The conditions for activation described above do not need to hold for a hit compound for mechanism-based activation. A hit compound may be defined as one that satisfies a subset of the conditions enumerated above, and may also display comparatively little inhibition in the

Fig 3. Mechanism-based activation of sirtuin enzymes: predicted steady-state properties and dose-response behavior. (A) Double reciprocal plots for deacylation initial rate measurements in the presence of activator. The blue box on the y-axis highlights the data that is used to construct the Dixon plot at saturating [NAD + ] depicted in (B). (B) Dixon plots for deacylation initial rate measurements in the presence of activator. The arrows point to predicted plateaus in these curves. (C) Comparison of double reciprocal plots at [NAM] = 0 /uni03BCM in the presence and absence of activator. (D) Comparison of Dixon plots at 1/ [NAD + ] = 0 in the presence and absence of activator. 'A' denotes a mechanism-based sirtuin activating compound. Note that the model depicted omits the term quadratic in [NAM] in Eq (1) and the plateaus/dotted lines shown in the Dixon plots are the asymptotic values to which the model-predicted rates converge in the absence of this term.

<!-- image -->

https://doi.org/10.1371/journal.pone.0194175.g003

<!-- image -->

pre-steady state burst phase. Such compounds may be capable of undergoing further improvement for substrate-specific activation of sirtuins like SIRT3, under physiologically relevant NAD + depletion conditions. For example, it is possible that catalytic efficiency does not increase in the absence of NAM, but does so in its presence (for example, due to increase in the K3 parameter above). Note that due to nonzero physiological concentration of NAM in the cell, reduction of NAM inhibition can also contribute to activation under physiologically relevant conditions. Alternatively, the relative rates of deacylation in the presence and absence of modulator could converge under certain combinations of [NAD + ] and [NAM].

## Potential means of increasing k 2

From the standpoint of chemical mechanisms of activation, the theory presented raises the important question of how the NAM cleavage rate k 2 of sirtuins can be accelerated by a ligand that binds to the various complexes in the deacylation reaction with the specified relative affinities, as predicted by equation in Fig 2a. It is important to note in this regard that the NAM cleavage reaction in sirtuins is generally believed to be endothermic, which enables effective NAMinhibition of the reaction [32, 45]. Unlike exothermic reactions, stabilization of products in endothermic reactions can decrease the activation barrier for the forward reaction, due to the fact that the transition state resembles the products more than the reactants. The energetics of this reaction, including the role of protein conformational changes, are being studied computationally in our group for mammalian sirtuins.

## Discussion

Wehave presented a model for activation of sirtuin enzymes suitable for the design and characterization of MB-STACs. Using this modeling framework, we have shown how modulation of K m ; NAD GLYPH<135> can in principle increase the activity of sirtuins. This activation can also apply in the presence of NAM, decreasing the sensitivity of the sirtuin to physiological NAM inhibition in addition to increasing its sensitivity to physiological NAD + . The mechanism of action of recently reported nonallosteric activators of sirtuins, such as honokiol (HKL) [28], which was reported to be a SIRT3 activator, and other compounds recently reported to activate SIRT5 and SIRT6 [30], can be characterized using the methods presented.

The rapid equilibrium segments approximation (Fig 2) was applied in order to illustrate how a ligand that binds outside the NAD + binding site can in principle increase sirtuin activity through only modulation of the relative free energies of the various species in the reaction mechanism. More detailed analysis of the mechanism of action of hit compounds for mechanism-based enzyme activation can be achieved by complete kinetic characterization in presence/absence of the activator, as discussed further below.

Structurally, binding outside of the NAD + binding site (the so-called A and C pockets [31, 46]) appears to be essential for mechanism-based activation. For example, consider the binding sites of long-chain fatty acids and Ex-527 [23, 44]. Rational design will require analysis of the relative free energies of complexes depicted in Fig 1. We have recently initiated computational studies [35] that assess such free energy differences for some of the front face (apo) complexes in this Fig 1, and further studies are in progress.

Structure-activity relationships for mechanism-based enzyme activating compounds are very different from those for allosteric activators. The kinetic effects of allosteric activators that operate through either reduction of substrate Kd or increase in k cat are mediated through global conformational changes that generally do not involve competing effects on steady state constants. Molecules that bind to allosteric sites will generally bind differentially to the

<!-- image -->

intermediates in a predetermined way (with specified Kd ratios) irrespective of their structural details; the same conformational change is induced by binding, irrespective of structure.

In mechanism-based activation, the kinetic effects of the activator depend on modulation of local degrees of freedom in the active site, not global conformational changes described by principal components. Typically, mechanism-based activators may alter the distributions of local degrees of freedom whose conformations change during the course of the reaction, which leads to tradeoffs in the ΔΔ G's for various reactions steps upon stabilization of one such conformation. As discussed above, activators of sirtuin enzymes that do not possess an allosteric site [13, 30, 44] have been shown crystallographically to induce changes in the conformation of the flexible cofactor binding loop in sirtuin enzymes. This loop changes conformation after the first chemical step of the reaction, namely the cleavage of nicotinamide from the NAD + cofactor. In these cases, the local degrees of freedom above are the backbone and side chain degrees of freedom in the flexible cofactor binding loop. Perhaps the most detailed structural studies on conformational changes in sirtuins induced by modulators have been reported for the mechanism-based inhibitor Ex-527, discussed above.

By inducing changes in the probability distributions of local active site degrees of freedom (DOF), the differential binding affinities of an activator ('A') to the various intermediates in the catalytic mechanism induce effects on the free energy differences ΔΔ G's) in that mechanism. We have already considered above the effect of arbitrary concentrations of a modulator Aon activity given specified Kdi , A's of modulator binding to different intermediates. The impact of a modulator A on the free energy differences relevant to catalytic mechanism can be represented in terms of a potential of mean force (PMF) that alters the probabilities of various receptor states in the conformational ensemble, and hence alters the catalytic free energy differences. The PMF only changes due to deviations of the specified local DOF, and can be calculated for any given modulator structure by using the corresponding molecular Hamiltonian to evaluate the average interaction potential in terms of these local DOF. Then, the effect of the modulator A on the binding free energy of a ligand (e.g., substrate) can be expressed in terms of the exponential mean of the PMF, providing structure-activity relations solely in terms of this PMF. Details of these calculations will be provided in future work.

## Conclusions

The enzyme activation theory presented herein enables the identification and evolution of important hits that may be inhibitors, not activators, by decomposing the observed kinetic effects of a modulator into components and identifying those molecules that display favorable values of a subset of these components as hits even if the net effect on catalytic turnover is inhibition. Such workflows would be fundamentally different from traditional drug discovery workflows and would bear more similarity to the directed evolution of enzymes. The theory presented also establishes foundations for the rational design of sirtuin-activating compounds, enabling the application of state-of-the-art computational methods to activator design in a manner analogous to computational enzyme design [47]. Once crystal structures solved, enzyme engineering methods can be used for hit to lead evolution based on the above theory.

To evolve such hit compounds into enzyme activators, computational design methods using high-resolution protein force fields [35, 47] can be applied in conjunction with experimental learning algorithms, such as directed evolution. Typically, the overall catalytic activity is used in directed evolution algorithms because it is the only quantity that can be efficiently measured in the laboratory. The ability to rapidly estimate the multiple free energy differences that determine catalytic activity through system identification methods [36] would allow multiobjective directed evolution algorithms to be applied in the laboratory. With system

<!-- image -->

identification, the parameter estimates can be used with such evolutionary algorithms to sample the nondominated Pareto frontier of Hamiltonian designs [48].

Aframework for catalyst system identification was proposed in [36]. This framework can be applied in the context of hit-to-lead evolution for mechanism-based activators, where the Hamiltonian is iteratively updated and catalytic free energy differences automatically estimated for each modulator Hamiltonian. The catalyst system identification framework can be automated using programmable logic and fluidic control systems in order to achieve a highthroughput implementation, as described in our recent publication [36].

In computational modulator design [47], where focused libraries of mutations may be generated, free energy differences calculated from mixed quantum/molecular mechanics (QM/ MM)methods for reactive chemistry and free energies of binding for substrate/product binding calculated using free energy perturbation can be compared to free energy data obtained using system identification for all steps of the catalytic mechanism. Computationally efficient predictions of free energy differences, especially those for binding events, must be calibrated through correlations with experimental data. The experimental estimates rapidly provided by system identification for any catalytically relevant free energy difference can be used for calibration.

Once the catalyst without Hamiltonian modulation (e.g., the wild-type enzyme) is accurately characterized, all other modulated systems can be characterized in terms of the ratios of k i' s or equivalently the ΔΔ Gs, which are used in high-throughput evolutionary algorithms as described in [36].

## Appendix A1

Steady state parameters of sirtuin-catalyzed deacylation expressed in terms of rate constants in the enzymatic reaction mechanism (Eq (2))

Kex = k -2 /k 2 , and the approximations refer to the case where k4 GLYPH<28> kj , j 6GLYPH<136> 4.

v max GLYPH<136> k 4 GLYPH<3> k 2 k GLYPH<0> 3 GLYPH<133> k GLYPH<0> 3 GLYPH<135> k 4 GLYPH<134> k GLYPH<0> 3 k 2 k GLYPH<0> 3 GLYPH<135> k 4 GLYPH<133> k GLYPH<0> 3 k 4 GLYPH<135> k GLYPH<0> 3 k GLYPH<0> 3 GLYPH<135> k GLYPH<0> 3 k GLYPH<0> 2 GLYPH<135> k GLYPH<0> 3 k 2 GLYPH<135> k 2 k 4 GLYPH<134> GLYPH<137> E GLYPH<138> 0 GLYPH<25> k 4 GLYPH<137> E GLYPH<138> 0 GLYPH<133> 11 GLYPH<134>

K m ; NAD GLYPH<135> GLYPH<136> v max GLYPH<137> E GLYPH<138> 0 k 2 k GLYPH<0> 3 GLYPH<135> k GLYPH<0> 1 k GLYPH<0> 3 GLYPH<135> k GLYPH<0> 1 k GLYPH<0> 2 GLYPH<135> k 2 k 4 GLYPH<135> k GLYPH<0> 1 k 4 k 1 k 2 GLYPH<133> k GLYPH<0> 3 GLYPH<135> k 4 GLYPH<134> GLYPH<25> k 4 1 k 1 GLYPH<135> K d ; NAD GLYPH<135> k GLYPH<0> 3 GLYPH<135> k GLYPH<0> 2 k GLYPH<0> 3 k 2 GLYPH<18> GLYPH<19> GLYPH<133> 12 GLYPH<134>

1 K 1 GLYPH<136> k 3 k GLYPH<0> 3 GLYPH<135> k 4 GLYPH<25> 1 K d ; NAM GLYPH<133> 13 GLYPH<134>

1 K 2 GLYPH<136> 1 K m ; NAD GLYPH<135> k 3 GLYPH<137> k GLYPH<0> 1 GLYPH<133> k GLYPH<0> 2 k GLYPH<0> 3 GLYPH<135> k 4 k GLYPH<0> 2 GLYPH<135> 2 k 4 k GLYPH<0> 3 GLYPH<134> GLYPH<135> k 4 GLYPH<133> k 2 k 4 GLYPH<135> k GLYPH<0> 1 k 4 GLYPH<135> 2 k GLYPH<0> 3 k 2 GLYPH<134>GLYPH<138> k 1 GLYPH<137> k GLYPH<0> 3 k 2 k GLYPH<0> 3 GLYPH<135> k 4 GLYPH<133> k GLYPH<0> 3 k 4 GLYPH<135> k GLYPH<0> 3 k GLYPH<0> 3 GLYPH<135> k GLYPH<0> 3 k GLYPH<0> 2 GLYPH<135> k GLYPH<0> 3 k 2 GLYPH<135> k 1 k 4 GLYPH<134>GLYPH<138> GLYPH<25> K d ; NAD GLYPH<135> K ex K m ; NAD GLYPH<135> K d ; NAM GLYPH<133> 14 GLYPH<134>

1 K 1 GLYPH<17> 1 a K 2 GLYPH<136> k 3 GLYPH<137> k GLYPH<0> 3 GLYPH<133> k GLYPH<0> 2 GLYPH<135> k 2 GLYPH<135> k 4 GLYPH<134> GLYPH<135> k 4 k 2 GLYPH<138> k GLYPH<0> 3 GLYPH<137> k GLYPH<0> 3 k 2 GLYPH<135> k 4 k 4 GLYPH<135> k GLYPH<0> 3 k 4 GLYPH<135> k 4 k GLYPH<0> 2 GLYPH<135> k 4 k 2 GLYPH<138> GLYPH<135> k 4 k 4 k 2 GLYPH<25> 1 GLYPH<135> K ex K d ; NAM GLYPH<133> 15 GLYPH<134>

<!-- image -->

## Appendix A2

Expressions for c ij 's in Eq (1):

c 11 GLYPH<136> k 4 k GLYPH<0> 3 GLYPH<137> k 4 k 2 GLYPH<135> k 4 k GLYPH<0> 1 GLYPH<135> k 2 k GLYPH<0> 3 GLYPH<135> k GLYPH<0> 1 k GLYPH<0> 3 GLYPH<135> k GLYPH<0> 2 k GLYPH<0> 1 GLYPH<138> GLYPH<133> 16 GLYPH<134>

c 12 GLYPH<136> k 3 k GLYPH<0> 2 k GLYPH<0> 1 k GLYPH<0> 2 GLYPH<135> k 4 GLYPH<133> k 2 k GLYPH<0> 3 k 3 GLYPH<135> k GLYPH<0> 1 k GLYPH<0> 3 k 3 GLYPH<134> GLYPH<133> 17 GLYPH<134>

c 21 GLYPH<136> k 4 GLYPH<133> k GLYPH<0> 3 k 1 k 4 GLYPH<135> k GLYPH<0> 3 k 1 k GLYPH<0> 3 GLYPH<135> k GLYPH<0> 3 k 1 k GLYPH<0> 2 GLYPH<134> GLYPH<133> 18 GLYPH<134>

c 22 GLYPH<136> k 1 k 3 k GLYPH<0> 2 k GLYPH<0> 3 GLYPH<135> k 4 k 1 k 3 k GLYPH<0> 3 GLYPH<133> 19 GLYPH<134>

c 31 GLYPH<136> k 4 k 1 k 2 k GLYPH<0> 3 GLYPH<133> 20 GLYPH<134>

c 32 GLYPH<136> k 1 k 2 k 3 k GLYPH<0> 3 GLYPH<133> 21 GLYPH<134>

c 41 GLYPH<136> k 1 k 2 k GLYPH<0> 3 k GLYPH<0> 3 GLYPH<133> 22 GLYPH<134>

c 51 GLYPH<136> k 4 k 1 k 2 k 4 GLYPH<133> 23 GLYPH<134>

c 52 GLYPH<136> k 4 GLYPH<133> k 4 k 3 k 2 GLYPH<135> k 4 k GLYPH<0> 1 k 3 GLYPH<135> k GLYPH<0> 3 k 3 k 2 GLYPH<135> k GLYPH<0> 2 k GLYPH<0> 1 k 3 GLYPH<135> k GLYPH<0> 2 k GLYPH<0> 1 k 3 GLYPH<134> GLYPH<133> 24 GLYPH<134>

c 53 GLYPH<136> k 4 k 1 k 2 k 3 GLYPH<133> 25 GLYPH<134>

c 54 GLYPH<136> k GLYPH<0> 2 k GLYPH<0> 1 k 3 k 3 GLYPH<135> k 4 GLYPH<133> k 2 k 3 k 3 GLYPH<135> k GLYPH<0> 1 k 3 k 3 GLYPH<134> GLYPH<133> 26 GLYPH<134>

## Supporting information

S1 Fig. Chemical mechanism of sirtuin-catalyzed deacylation and modes of sirtuin activation. Following sequential binding of acylated peptide substrate and NAD + cofactor, the reaction proceeds in two consecutive stages: i) cleavage of the NAM moiety of NAD + (ADPribosyl transfer) through the nucleophilic attack of the acetyl-Lys side chain of the protein substrate to form a positively charged O-alkylimidate intermediate, and ii) subsequent formation of deacylated peptide. For simplicity, all steps of stage ii as well as AADPR + Pr dissociation are depicted to occur together with rate limiting constant k4 . The schematic highlights mechanism-based activation through NAD + Km reduction rather than the Kd peptide reduction that known allosteric sirtuin activators elicit. (TIF)

S2 Fig. General model for sirtuin-catalyzed deacylation in the presence of NAD + and NAM. This provides a minimal kinetic model that captures the essential features of sirtuin deacylation kinetics suitable for predicting the effects of mechanism-based modulators on sirtuin activity. In the presence of saturating Ac-Pr, E is rapidly converted into E.Ac-Pr and NAMbinding to E can be neglected, resulting in a simplified reaction network with 5 species. Ac-Pr, acetylated peptide; ADPR, adenosine diphosphate ribose; AADPR, O-acetyl adenosine diphosphate ribose. (TIF)

<!-- image -->

S1 File. Steady state constant and rapid equilibrium segments expressions. (DOCX)

## Author Contributions

Conceptualization: Raj Chakrabarti.

Formal analysis: Xiangying Guan, Alok Upadhyay, Sudipto Munshi, Raj Chakrabarti.

Methodology: Xiangying Guan, Alok Upadhyay, Sudipto Munshi, Raj Chakrabarti.

Supervision: Raj Chakrabarti.

Writing - original draft: Raj Chakrabarti.

Writing - review & editing: Xiangying Guan, Alok Upadhyay.

## References

- 1. Kaeberlein M, McVey M, Guarente L. The SIR2/3/4 complex and SIR2 alone promote longevity in Saccharomyces cerevisiae by two different mechanisms. Genes & Development. 1999; 13(19):2570-80. https://doi.org/10.1101/gad.13.19.2570
- 2. Hirsch BM, Zheng W. Sirtuin mechanism and inhibition: explored with N(epsilon)-acetyl-lysine analogs. Molecular bioSystems. 2011; 7(1):16-28. https://doi.org/10.1039/c0mb00033g PMID: 20842312.
- 3. Cen Y. Sirtuins inhibitors: the approach to affinity and selectivity. Biochimica et biophysica acta. 2010; 1804(8):1635-44. https://doi.org/10.1016/j.bbapap.2009.11.010 PMID: 19931429.
- 4. Sauve AA. Sirtuin chemical mechanisms. Biochimica Et Biophysica Acta-Proteins and Proteomics. 2010; 1804(8):1591-603. https://doi.org/10.1016/j.bbapap.2010.01.021 PMID: 20132909
- 5. Hu P, Wang S, Zhang Y. Highly dissociative and concerted mechanism for the nicotinamide cleavage reaction in Sir2Tm enzyme suggested by ab initio QM/MM molecular dynamics simulations. Journal of the American Chemical Society. 2008; 130(49):16721-8. https://doi.org/10.1021/ja807269j PMID: 19049465.
- 6. Zhou Y, Zhang H, He B, Du J, Lin H, Cerione RA, et al. The bicyclic intermediate structure provides insights into the desuccinylation mechanism of human sirtuin 5 (SIRT5). The Journal of biological chemistry. 2012; 287(34):28307-14. https://doi.org/10.1074/jbc.M112.384511 PMID: 22767592.
- 7. Jackson MD, Schmidt MT, Oppenheimer NJ, Denu JM. Mechanism of nicotinamide inhibition and transglycosidation by Sir2 histone/protein deacetylases. The Journal of biological chemistry. 2003; 278 (51):50985-98. https://doi.org/10.1074/jbc.M306552200 PMID: 14522996.
- 8. Smith BC, Denu JM. Sir2 protein deacetylases: evidence for chemical intermediates and functions of a conserved histidine. Biochemistry. 2006; 45(1):272-82. https://doi.org/10.1021/bi052014t PMID: 16388603.
- 9. Smith BC, Denu JM. Sir2 deacetylases exhibit nucleophilic participation of acetyl-lysine in NAD+ cleavage. Journal of the American Chemical Society. 2007; 129(18):5802-3. https://doi.org/10.1021/ ja070162w PMID: 17439123.
- 10. Mercken EM, Mitchell SJ, Martin-Montalvo A, Minor RK, Almeida M, Gomes AP, et al. SRT2104 extends survival of male mice on a standard diet and preserves bone and muscle mass. Aging Cell. 2014; 13(5):787-96. Epub 2014/06/17. https://doi.org/10.1111/acel.12220 PMID: 24931715
- 11. Mitchell SJ, Martin-Montalvo A, Mercken EM, Palacios HH, Ward TM, Abulwerdi G, et al. The SIRT1 activator SRT1720 extends lifespan and improves health of mice fed a standard diet. Cell reports. 2014; 6(5):836-43. Epub 2014/03/04. https://doi.org/10.1016/j.celrep.2014.01.031 PMID: 24582957.
- 12. Zorn JA, Wells JA. Turning enzymes ON with small molecules. Nature chemical biology. 2010; 6 (3):179-88. Epub 2010/02/16. https://doi.org/10.1038/nchembio.318 PMID: 20154666.
- 13. Hubbard BP, Gomes AP, Dai H, Li J, Case AW, Considine T, et al. Evidence for a Common Mechanism of SIRT1 Regulation by Allosteric Activators. Science. 2013; 339(6124):1216-9. https://doi.org/10. 1126/science.1231097 PMID: 23471411
- 14. Dai H, Case AW, Riera TV, Considine T, Lee JE, Hamuro Y, et al. Crystallographic structure of a small molecule SIRT1 activator-enzyme complex. Nat Commun. 2015; 6:7645. Epub 2015/07/03. https://doi. org/10.1038/ncomms8645 PMID: 26134520.

<!-- image -->

- 15. Lakshminarasimhan M, Rauh D, Schutkowski M, Steegborn C. Sirt1 activation by resveratrol is substrate sequence-selective. Aging (Albany NY). 2013; 5(3):151-4. https://doi.org/10.18632/aging. 100542 PMID: 23524286.
- 16. Dittenhafer-Reed KE, Feldman JL, Denu JM. Catalysis and mechanistic insights into sirtuin activation. Chembiochem: a European journal of chemical biology. 2011; 12(2):281-9. https://doi.org/10.1002/ cbic.201000434 PMID: 21243715.
- 17. Lakshminarasimhan M, Rauh D, Schutkowski M, Steegborn C. Sirt1 activation by resveratrol is substrate sequence-selective. Aging-Us. 2013; 5(3):151-4.
- 18. Borra MT, Smith BC, Denu JM. Mechanism of human SIRT1 activation by resveratrol. Journal of Biological Chemistry. 2005; 280(17):17187-95. https://doi.org/10.1074/jbc.M501250200 PMID: 15749705
- 19. Sinclair DA, Guarente L. Small-Molecule Allosteric Activators of Sirtuins. Annual review of pharmacology and toxicology. 2014; 54:363-80. https://doi.org/10.1146/annurev-pharmtox-010611-134657 PMID: 24160699.
- 20. North BJ, Rosenberg MA, Jeganathan KB, Hafner AV, Michan S, Dai J, et al. SIRT2 induces the checkpoint kinase BubR1 to increase lifespan. Embo Journal. 2014; 33(13):1438-53. https://doi.org/10. 15252/embj.201386907 PMID: 24825348
- 21. Brown K, Xie S, Qiu X, Mohrin M, Shin J, Liu Y, et al. SIRT3 reverses aging-associated degeneration. Cell reports. 2013; 3(2):319-27. Epub 2013/02/05. https://doi.org/10.1016/j.celrep.2013.01.005 PMID: 23375372.
- 22. Kanfi Y, Naiman S, Amir G, Peshti V, Zinman G, Nahum L, et al. The sirtuin SIRT6 regulates lifespan in male mice. Nature. 2012; 483(7388):218-21. Epub 2012/03/01. https://doi.org/10.1038/nature10815 PMID: 22367546.
- 23. Gertz M, Fischer F, Nguyen GTT, Lakshminarasimhan M, Schutkowski M, Weyand M, et al. Ex-527 inhibits Sirtuins by exploiting their unique NAD(+)-dependent deacetylation mechanism. Proceedings of the National Academy of Sciences of the United States of America. 2013; 110(30):E2772-E81. https:// doi.org/10.1073/pnas.1303628110 PMID: 23840057
- 24. Rumpf T, Schiedel M, Karaman B, Roessler C, North BJ, Lehotzky A, et al. Selective Sirt2 inhibition by ligand-induced rearrangement of the active site. Nat Commun. 2015; 6:6263. Epub 2015/02/13. https:// doi.org/10.1038/ncomms7263 PMID: 25672491
- 25. Smith BC, Denu JM. Mechanism-based inhibition of Sir2 deacetylases by thioacetyl-lysine peptide. Biochemistry. 2007; 46(50):14478-86. Epub 2007/11/22. https://doi.org/10.1021/bi7013294 PMID: 18027980.
- 26. Canto C, Houtkooper RH, Pirinen E, Youn DY, Oosterveer MH, Cen Y, et al. The NAD(+) precursor nicotinamide riboside enhances oxidative metabolism and protects against high-fat diet-induced obesity. Cell Metab. 2012; 15(6):838-47. Epub 2012/06/12. https://doi.org/10.1016/j.cmet.2012.04.022 PMID: 22682224
- 27. Mai A, Valente S, Meade S, Carafa V, Tardugno M, Nebbioso A, et al. Study of 1,4-Dihydropyridine Structural Scaffold: Discovery of Novel Sirtuin Activators and Inhibitors. Journal of Medicinal Chemistry. 2009; 52(17):5496-504. https://doi.org/10.1021/jm9008289 PMID: 19663498
- 28. Pillai VB, Samant S, Sundaresan NR, Raghuraman H, Kim G, Bonner MY, et al. Honokiol blocks and reverses cardiac hypertrophy in mice by activating mitochondrial Sirt3. Nat Commun. 2015; 6:6656. Epub 2015/04/15. https://doi.org/10.1038/ncomms7656 PMID: 25871545
- 29. Valente S, Mellini P, Spallotta F, Carafa V, Nebbioso A, Polletta L, et al. 1,4-Dihydropyridines Active on the SIRT1/AMPK Pathway Ameliorate Skin Repair and Mitochondrial Function and Exhibit Inhibition of Proliferation in Cancer Cells. Journal of Medicinal Chemistry. 2016; 59(4):1471-91. https://doi.org/10. 1021/acs.jmedchem.5b01117 PMID: 26689352
- 30. You W, Rotili D, Li TM, Kambach C, Meleshin M, Schutkowski M, et al. Structural Basis of Sirtuin 6 Activation by Synthetic Small Molecules. Angewandte Chemie (International ed in English). 2017; 56 (4):1007-11. Epub 2016/12/19. https://doi.org/10.1002/anie.201610082 PMID: 27990725.
- 31. Avalos JL, Boeke JD, Wolberger C. Structural basis for the mechanism and regulation of Sir2 enzymes. Molecular Cell. 2004; 13(5):639-48. https://doi.org/10.1016/s1097-2765(04)00082-6 PMID: 15023335
- 32. Liang Z, Shi T, Ouyang S, Li H, Yu K, Zhu W, et al. Investigation of the catalytic mechanism of Sir2 enzyme with QM/MM approach: SN1 vs SN2? The journal of physical chemistry B. 2010; 114 (36):11927-33. https://doi.org/10.1021/jp1054183 PMID: 20726530.
- 33. Shi YW, Zhou YZ, Wang SL, Zhang YK. Sirtuin Deacetylation Mechanism and Catalytic Role of the Dynamic Cofactor Binding Loop. J Phys Chem Lett. 2013; 4(3):491-5. https://doi.org/10.1021/ jz302015s PMID: 23585919

<!-- image -->

- 34. Avalos JL, Bever KM, Wolberger C. Mechanism of sirtuin inhibition by nicotinamide: Altering the NAD (+) cosubstrate specificity of a Sir2 enzyme. Molecular Cell. 2005; 17(6):855-68. https://doi.org/10. 1016/j.molcel.2005.02.022 PMID: 15780941
- 35. Guan X, Lin P, Knoll E, Chakrabarti R. Mechanism of inhibition of the human sirtuin enzyme SIRT3 by nicotinamide: computational and experimental studies. PLoS One. 2014; 9(9):e107729. Epub 2014/09/ 16. https://doi.org/10.1371/journal.pone.0107729 PMID: 25221980
- 36. Guan X, Chakrabarti R. Molecular system identification for enzyme directed evolution and design. The Journal of chemical physics. 2017; 147(12):124106. Epub 2017/10/02. https://doi.org/10.1063/1. 4996838 PMID: 28964026.
- 37. Cen Y, Sauve AA. Transition state of ADP-ribosylation of acetyllysine catalyzed by Archaeoglobus fulgidus Sir2 determined by kinetic isotope effects and computational approaches. Journal of the American Chemical Society. 2010; 132(35):12286-98. https://doi.org/10.1021/ja910342d PMID: 20718419.
- 38. Feldman JL, Dittenhafer-Reed KE, Kudo N, Thelen JN, Ito A, Yoshida M, et al. Kinetic and Structural Basis for Acyl-Group Selectivity and NAD+ Dependence in Sirtuin-Catalyzed Deacylation. Biochemistry. 2015; 54(19):3037-50. https://doi.org/10.1021/acs.biochem.5b00150 PMID: 25897714
- 39. Sauve AA, Moir RD, Schramm VL, Willis IM. Chemical activation of Sir2-dependent silencing by relief of nicotinamide inhibition. Molecular Cell. 2005; 17(4):595-601. https://doi.org/10.1016/j.molcel.2004.12. 032 PMID: 15721262
- 40. Hawse WF, Hoff KG, Fatkins D, Daines A, Zubkova OV, Schramm VL, et al. Structural Insights Into Intermediate Steps in the Sir2 Deacetylation Reaction. Structure. 2008; 16(9):1368-77. https://doi.org/ 10.1016/j.str.2008.05.015 PMID: 18786399
- 41. Armstrong CM, Kaeberlein M, Imai SI, Guarente L. Mutations in Saccharomyces cerevisiae gene SIR2 can have differential effects on in vivo silencing phenotypes and in vitro histone deacetylation activity. Mol Biol Cell. 2002; 13(4):1427-38. Epub 2002/04/16. https://doi.org/10.1091/mbc.01-10-0482 PMID: 11950950
- 42. Szczepankiewicz BG, Dai H, Koppetsch KJ, Qian D, Jiang F, Mao C, et al. Synthesis of carba-NAD and the structures of its ternary complexes with SIRT3 and SIRT5. The Journal of organic chemistry. 2012; 77(17):7319-29. Epub 2012/08/02. https://doi.org/10.1021/jo301067e PMID: 22849721.
- 43. Zhao KH, Harshaw R, Chai XM, Marmorstein R. Structural basis for nicotinamide cleavage and ADPribose transfer by NAD(+)-dependent Sir2 histone/protein deacetylases. Proceedings of the National Academy of Sciences of the United States of America. 2004; 101(23):8563-8. https://doi.org/10.1073/ pnas.0401057101 PMID: 15150415
- 44. Feldman JL, Baeza J, Denu JM. Activation of the protein deacetylase SIRT6 by long-chain fatty acids and widespread deacylation by mammalian sirtuins. The Journal of biological chemistry. 2013; 288 (43):31350-6. Epub 2013/09/21. https://doi.org/10.1074/jbc.C113.511261 PMID: 24052263.
- 45. Sauve AA, Schramm VL. Sir2 regulation by nicotinamide results from switching between base exchange and deacetylation chemistry. Biochemistry. 2003; 42(31):9249-56. https://doi.org/10.1021/ bi034959l PMID: 12899610.
- 46. Hawse WF, Wolberger C. Structure-based Mechanism of ADP-ribosylation by Sirtuins. Journal of Biological Chemistry. 2009; 284(48):33654-61. https://doi.org/10.1074/jbc.M109.024521 PMID: 19801667
- 47. Chakrabarti R, Klibanov AM, Friesner RA. Sequence optimization and designability of enzyme active sites. Proc Natl Acad Sci U S A. 2005; 102(34):12035-40. Epub 2005/08/17. https://doi.org/10.1073/ pnas.0505397102 PMID: 16103370.
- 48. Brif C, Chakrabarti R, Rabitz H. Control of quantum phenomena: past, present and future. New Journal of Physics. 2010; 12(7):075008.