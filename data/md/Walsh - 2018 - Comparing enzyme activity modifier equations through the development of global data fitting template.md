<!-- image -->

<!-- image -->

Submitted 18 July 2017 Accepted 7 November 2018 Published 14 December 2018

Corresponding author Ryan Walsh, ryan.walsh@iaf.inrs.ca

Academic editor Paul Tulkens

Additional Information and Declarations can be found on page 22

DOI 10.7717/peerj.6082

Copyright

2018 Walsh

Distributed under Creative Commons CC-BY 4.0

OPEN ACCESS

## Comparing enzyme activity modifier equations through the development of global data fitting templates in Excel

Ryan Walsh

Microbiology/Biochemistry, INRSGLYPH<21>Institut Armand-Frappier, Laval, Quebec, Canada

## ABSTRACT

The classical way of defining enzyme inhibition has obscured the distinction between inhibitory effect and the inhibitor binding constant. This article examines the relationship between the simple binding curve used to define biomolecular interactions and the standard inhibitory term (1 C ( T I U = Ki )). By understanding how this term relates to binding curves which are ubiquitously used to describe biological processes, a modifier equation which distinguishes between inhibitor binding and the inhibitory effect, is examined. This modifier equation which can describe both activation and inhibition is compared to standard inhibitory equations with the development of global data fitting templates in Excel and via the global fitting of these equations to simulated and previously published datasets. In both cases, this modifier equation was able to match or outperform the other equations by providing superior fits to the datasets. The ability of this single equation to outperform the other equations suggests an over-complication of the field. This equation and the template developed in this article should prove to be useful tools in the study of enzyme inhibition and activation.

Subjects Biochemistry, Computational Biology, Mathematical Biology, Drugs and Devices, Pharmacology

Keywords Enzyme inhibition, Enzyme activation, Global data fitting, Model comparison, Drug development, Inhibition constant

## INTRODUCTION

The historical development of enzyme-inhibitory theory relied on the generation of rapid equilibrium inhibitory equations akin to the derivation of the MichaelisGLYPH<21>Menten equation. These equations developed inhibitory theory around a single constant, termed the inhibition constant ( Ki ), which when inserted into the MichaelisGLYPH<21>Menten equation (Eq. 1; Michaelis & Menten, 1913 ), in various ways, was used to describe apparent shifts in measured values of the maximum reaction rate ( V max) and the Michaelis constant ( KM ) ( McElroy, 1947 ).

v D [ S ] [ S ] C KM V max : (1)

The MichaelisGLYPH<21>Menten equation (Eq. 1) shares the same mathematical structure as the Hill-Langmuir equation (Eq. 2) or ligandGLYPH<21>receptor binding relationship (Eq. 3; Gesztelyi et al., 2012 ). The main difference is that the MichaelisGLYPH<21>Menten equation describes the rate of catalytic turnover by an enzyme, where chemical bonds are broken or formed, rather than

strictly molecular associations such as the binding between ligand and receptor (Eq. 3) or the binding of molecules to a surface as in the case of the Hill-Langmuir equation (Eq. 2).

GLYPH<18> D [ L ] n [ L ] n C Kd (2)

Receptor binding D [ L ] [ L ] C Kd : (3)

These equations all take the same form, relating a change in response or signal ( v , GLYPH<30> , receptor binding), to the concentration of a substance ([S], [L]) based on a constant ( KM , Kd ) that is itself defined as a concentration of that substance. For example, in the MichaelisGLYPH<21> Menten equation, the fraction of the total possible enzymatic conversion of substrate to product ( v ) is determined by the substrate binding affinity, the Michaelis constant ( KM ). The substrate binding affinity is the concentration at which the reaction velocity ( v ) is half that of the theoretical maximum reaction rate ( V max). This relationship can be easily demonstrated by assuming that an enzyme with a KM value of 1 is exposed to a substrate concentration of 1 ( T S U D 1). This produces the situation where the substrate concentration of 1 is divided by itself plus the KM value of 1, yielding the V max multiplied by 1 2 . This association produces the hyperbolic relationship between compound concentration and response ubiquitously found in equations used to describe biological interactions (Fig. 1A). The simple relationship is derived from chemical equilibrium mass action relationships and in general, governs most interactions at the molecular level. This relationship has even been used to distill inhibitory theory down to its most basic form, IC50 values ( Sebaugh, 2011 ; Eq. 4), where the inhibitory binding constant is denoted as the concentration of inhibitor needed to reduce the target enzyme's activity by 50%.

%Inhibition D [ I ] [ I ] C IC50 GLYPH<2> 100 (4)

IC50 values are the most common way of characterizing inhibitors, as they provide an easy way of comparing the inhibitory potential of compounds being developed as new drug candidates. IC50 values however only describe changes in the enzyme's reaction rate ( v ) and are not an indication of variations in the maximal turnover ( V max) or substrate affinity ( KM ).

Traditionally, changes in reaction velocity produced by changes in substrate affinity and/or maximal velocity, have been defined with equations that were derived from reaction schemes based on enzyme, substrate and inhibitor interactions. This method of describing enzyme inhibition was highly dependent on the use of inhibition constants ( Ki ) which initially made its appearance in the competitive (Eq. 5), non-competitive (Eq. 6), uncompetitive (Eq. 7) and mixed non-competitive inhibition equations (Eq. 8) ( McElroy, 1947 ; Cleland, 1970 ).

v D [ S ] [ S ] C KM GLYPH<16> 1 C [ I ] GLYPH<17> V max (5)

Ki

v D [ S ] . [ S ] C KM / GLYPH<16> 1 C [ I ] Ki GLYPH<17> V max (6)

Modifier bound

Figure 1 Enzyme-substrate-modifier interactions. (A) Enzyme-substrate binding, like any bimolecular system where ligand is in excess, can be expressed using a hyperbolic binding curve. Similarly, hyperbolic binding curves are also useful for describing the binding of modifiers, either inhibitors or activators, with the enzyme. (B) A basic way of conceptualizing the rate at which an enzyme population hydrolyses its substrate and how that rate may be affected by modifiers, is to limit the potential states the enzymes may be found in to free enzyme, enzyme-substrate complex, enzyme-modifier complex and enzyme-substratemodifier complex. Catalysis is then defined by the portion of the (continued on next page...) Full-size DOI: 10.7717/peerj.6082/fig-1

<!-- image -->

## Figure 1 (...continued)

substrate bound population affected by modifier ( k cat2) or free of modifier ( k cat1). (C) The hyperbolic association of substrate (yellow boxes) and modifier (blue boxes) with the enzyme population is then able to provide a way of determining the rate of substrate catalysis. The depicted table is very similar to a simple multiplication table where the percent of substrate associated enzyme is displayed vertically with yellow bars, while association of modifier is displayed horizontally with blue bars. Overlap of the two populations is depicted as green, and along with the yellow bars represent the portion of the enzyme population which are catalytically relevant. While the hyperbolic curves described by the binding isotherm is a continuum between 0% and 100% association, the table is limited to 0%, 25%, 50%, 75% and 100% for simplicity. Substrate hydrolysis is then defined by the portion o the enzyme population associated with substrate in the presence or absence of modifier. For example, in the absence of modifier (0%), at a substrate concentration equal to the KM , 50% of the enzyme population is bound by substrate and the reaction rate is half that of the V MAX1. However, if a concentration of modifier equal to the modifier binding constant ( KX ) is added, half of the enzyme population is shifted to the new catalytic rate ( k cat2) and substrate affinity ( KM 2). This results in 25% of the population hydrolysing substrate free of modifier (Yellow box) and 25% shifted to the altered state (green box). The altered state produced by the modifier may result in a very different substrate association than that observed with the unmodified enzyme population, so it must be recognized that the green boxes represent the portion of the population that is altered by the modifier unlike the yellow boxes that represent substrate association and can be directly related to the V MAX1.

v D [ S ] [ S ] GLYPH<16> 1 C [ I ] Ki GLYPH<17> C KM V max (7)

v D [ S ] [ S ] GLYPH<16> 1 C [ I ] GLYPH<11> Ki GLYPH<17> C KM GLYPH<16> 1 C [ I ] Ki GLYPH<17> V max (8)

While these equations added both inhibition constants and terms for the inhibitor concentration to the MichaelisGLYPH<21>Menten equation, absent are terms defining the potential catalytic activity of the enzyme-inhibitor complex. This may be due to the mechanisms used in the derivation of these equations which do not take into account partial inhibition and have resulted in their designation as total inhibitors ( Cleland, 1970 ). To overcome this limitation, other equations have been developed to describe compounds that do not completely stop the catalytic activity of their target ( Bisswanger, 2002 ; Cleland, 1970 ; Segel, 1975 ; Yoshino, 1987 ). However, these equations, known as partial inhibition equations, are rarely utilized in the literature.

So what do the equations for total inhibition describe? An easy way of visualizing how these equations are believed to affect the activity of an enzyme is to plot experimentally determined values of V max and KM on a Cartesian coordinate graph with V max on the y -axis and KM on the x -axis (Fig. 2A). If the catalytic activity of an enzyme is defined as the coordinates KM and V max then inhibtion or activation of the enzyme's activity can be expressed as a shift to a different position on the graph. For example, the classical competitive inhibition equation (Eq. 5) represents a decrease in substrate binding resulting from the presence of a substrate mimic that blocks the enzymes active site. This is characterized by a decrease in apparent substrate affinity producing an increase in the apparent KM value from its initial value to infinity in a linear fashion (Fig. 2B). While, the non-competitive inhibition equation (Eq. 6), represents a hyperbolic decrease in V max from its initial value to zero (Fig. 2C). The uncompetitive equation (Eq. 7) causes an apparent reduction in the KM value implying a higher substrate affinity, while also

Figure 2 Cartesian coordinate plots. Cartesian coordinate plots of (A) the maximum velocity ( V max) and substrate affinity constants ( KM ) used to define the MichaelisGLYPH<21>Menten (B) the effect of competitive inhibition (C) non-competitive inhibition and (D) mixed non-competitive inhibition. (E) A representation of the full range of effects which may occur using Eq. (13) and (F) A plot of a theoretical compound which activates the catalytic rate while decreasing substrate affinity emphasizing the hyperbolic relationship that should govern a transition between any of the points on the Cartesian plot.

<!-- image -->

Full-size DOI: 10.7717/peerj.6082/fig-2

decreasing the apparent value of the V max (Fig. 2D). The mixed non-competitive inhibition equation (Eq. 8) produces a reduction in the V max while either increasing or decreasing the KM based on the ratio between Ki and Ki GLYPH<11> (Fig. 2E). The changes in enzymatic activity described by these equations leave many other undefined inhibitory and stimulatory possibilities (Fig. 2F). As previously stated, while these equations are the most common

forms of inhibition reported in the literature, aside from IC50s, their primary disadvantage is their inability to describe the activity of an enzyme-inhibitor complex. This has been addressed with the derivation of separate sets of equations to cover what is referred to as the partial forms of inhibition associated with each of the classical inhibition types, i.e., partial competitive, partial non-competitive, partial uncompetitive and partial mixed non-competitive ( Bisswanger, 2002 ; Cleland, 1970 ; Segel, 1975 ; Yoshino, 1987 ). To simplify and standardize the field Fontes, Ribeiro & Sillero (2000) and more recently Baici (2015) have attempted to redefine all the possible interactions inhibitors and activators may have with an enzyme. However, as the complexity of the proposed equations has continued to increase, their application has trailed off, with many journals now accepting or having a preference for IC50 values ( Brandt, Laux & Yates, 1987 ; Lazareno & Birdsall, 1993 ).

In my opinion, overcomplication of the enzyme modifier kinetics is contributing to the demise of the field and this overcomplication is related to the treatment of Ki in the total inhibitor equations (Eqs. 5GLYPH<21>8). In the total inhibitor equations, the Ki is equated to the effect of the inhibitor on the enzymatic activity rather than an equilibrium binding constant marking the concentration where half the enzyme population is bound by the inhibitor.

The arrangement of the Ki in the total inhibition equations is unusual, in that, while the general term (Eq. 9) appears to be the same in all of the equations (Eqs. 5GLYPH<21>8), it functions as a factor of the denominator in the non-competitive equation (Eq. 6) and as a factor of individual terms in the denominator with the other equations (Eqs. 5GLYPH<21>(8)). Additionally, this general term (Eq. 9) that is supposed to describe the binding of the inhibitor to the enzyme does not share the same format as other equations used to describe biological interactions (Eqs. 1GLYPH<21>4). However, a rearrangement of the non-competitive equation (Eq. 10) demonstrates that this notation is actually the reciprocal form of the hyperbolic equation used to describe biological interactions (Eq. 11; Walsh, 2012 ).

GLYPH<18> 1 C [ I ] Ki GLYPH<19> (9) v D [ S ] . [ S ] C KM / GLYPH<16> 1 C [ I ] Ki GLYPH<17> V max D [ S ] [ S ] C KM GLYPH<18> V max GLYPH<0> V max [ I ] [ I ] C Ki GLYPH<19> (10) (11)

1 GLYPH<16> 1 C [ I ] Ki GLYPH<17> D GLYPH<18> 1 GLYPH<0> [ I ] [ I ] C Ki GLYPH<19> :

This rearrangement (Eq. 10), directly relates the non-competitive equation's hyperbolic decrease in V max, to the binding of the inhibitor with the enzyme population. This rearrangement also explains why the non-competitive inhibition equation is limited to situations where the inhibitor completely stops the catalytic activity of the enzyme, as the V max is reduced by itself, as the inhibitor binds the enzyme population (Eq. 10). This alternate form of the inhibitory term also suggests a rationale for the odd pattern of the classic competitive inhibition equation. In the competitive equation (Eq. 5), the KM is multiplied by the inhibitory term (Eq. 9) resulting in the KM getting divided by the fraction of the enzyme population not bound by the inhibitor (Eq. 12). This produces the linear

trend of increasing KM driving its value to infinity rather than generating a hyperbolic shift from one substrate affinity to another. A one to one association of inhibitor with enzyme would mean that each enzyme bound by inhibitor expresses the new apparent KM value induced by the inhibitor. As the enzyme population is converted from an inhibitor-free group to an inhibitor bound group, the observed KM would shift from the initial KM to the inhibitor-induced apparent KM in a hyperbolic manner. Therefore, the competitive model cannot describe changes in KM resulting from a one to one association of the inhibitor with the enzyme.

v D [ S ] [ S ] C KM GLYPH<16> 1 C [ I ] Ki GLYPH<17> V max D [ S ] [ S ] C KM GLYPH<16> 1 GLYPH<0> [ I ] [ I ] C K i GLYPH<17> V max : (12)

While many inhibitors that only change substrate affinity are classified as competitive, it is not hard to envision situations where changes in enzyme-substrate binding could be caused by interactions not related to blockage of the enzyme's active site by an inhibitor which mimics the substrate. For example changes in the conformation of the active site could reduce the ability of the substrate to bind without reducing the catalytic rate of the enzyme. This could occur through alosteric interactions or even through partial blockade of the active site when the enzyme is associated with the inhibitor. For example, the peptidase kallikrein was believed to be competitively inhibited by benzamidine ( Sousa et al., 2001 ). However, the crystal structure of benzamidine binding to kallikrein demonstrated that it does not block the catalytic site of the enzyme but instead binds to a portion of the protease that deals with substrate specificity. Known as the side chain binding pocket, benzamidine binds to a portion of the enzyme which recognizes the side chain of phenylalanine ( Bernett et al., 2002 ). This results in a hyperbolic decrease in substrate affinity based on the portion of the kallikrein population bound to benzamidine. While each kallikrein enzyme bound by the benzamidine has less affinity for its substrate it still hydrolyses the substrate at the same rate. This is supported by a better fit of the experimental data to a hyperbolic rather than linear change in KM ( Walsh, Martin & Darvesh, 2011a ).

While inhibitor interactions that conform to the traditional competitive equation cannot be ruled out, the evidence for classifing an inhibitor as competitive must be closely scrutinized before the inhibition can be attributed to the standard competitive equation (Eq. 12).

Assuming that enzyme-inhibitor interactions are dependent on the same relationship which defines other molecular systems (Eqs. 1GLYPH<21>4), the MichaelisGLYPH<21>Menten equation can be modified to accommodate both positive and negative changes in KM and V max by adding terms which relate binding of the inhibitor with the enzyme population directly to change in enzymatic activity ( Walsh, Martin & Darvesh, 2007 ; Eq. 13).

v D [ S ] [ S ] C KM 1 GLYPH<0> . KM 1 GLYPH<0> KM 2 / [ X ] [ X ] C kx V max GLYPH<0> . V max GLYPH<0> V max / [ X ] [ X ] C kx (13)

In this equation, the changes from the initial KM and V max values are directly related to the binding of modifier ( X ) with the enzyme (Figs. 1B, 1C). The change from inhibitor to modifier notation refers to the ability of this equation to describe activators of enzymatic

activity as well as inhibitors. The numrical subscripts associated with the V max and KM are used to represent the distinct states of the enzyme. For example in the absence of modifier the V max and KM are denoted as V12ptmax1 and K M 1 while V12ptmax2 and KM 2 represent V max and KM values produced by the modifier. By clearly defining V12ptmax2 and KM2, this equation can be used to model either negative or positive changes in the V max and KM (Fig. 2F) provided the shifts are hyperbolic. As previously stated the designation of a V12ptmax2 stems from a simple rearrangement of the non-competitive inhibition equation (Eq. 10), while the term describing changes to the KM can be derived the same way the other classical equations have been derived, using the rate equation, conservation of mass and equilibrium relationships (Supplemental Information 1). Indeed, the main failing of this equation may be that it is unable to produce the linear increase in KM which characterizes the standard competitive inhibition equation (Fig. 2B). However, whether previously observed linear changes in KM are in fact linear or just represent the linear portion of a hyperbolic curve, (as it could be argued was the case with benzamidines' inhibition of kallikrein) deserves more attention ( Walsh, Martin & Darvesh, 2011a ).

## MATERIALS & METHODS

Templates for comparing inhibitor and activator equations were developed using Excel. All enzyme kinetic data analyzed in this study was collected from previously published results or simulated using the equations described. The ability of the equations to model the data was evaluated using non-linear regression with the solver add-in of Excel to globally fit the data ( Kemmer & Keller, 2010 ).

## RESULTS & DISCUSSION

To truly assess the fitting of an equation to experimental data the equation should be globally fit to the data. To this end, a template which can compare the capacity of the classical inhibition equations (Eqs. 5GLYPH<21>8) and the modifier equation (Eq. 13), to globally fit experimental data was developed (Supplemental Information 2). To illustrate the functionality of the template, data was acquired from Biotek's application note on basic enzyme kinetic determinations ( Held, 2007 ), where the inhibition of GLYPH<12> -galactosidase by GLYPH<12> -D-thiogalactopyranoside was examined. The structural similarity between the inhibitor and the substrate, combined with the pattern observed using a double reciprocal plot lead to the conclusion that GLYPH<12> -galactosidase was competitively inhibited by GLYPH<12> -D-thiogalactopyranoside ( Held, 2007 ). However, this analysis was based on standard pattern recognition where regression lines for each inhibitor concentration were overlaid and convergence of the lines close to the y -axis was interpreted as competitive inhibition. This sort of analysis does not determine whether the pattern produced by the regression lines conforms to a global fitting of the competitive inhibition equation (Eq. 12) to the experimental data. Indeed, this reliance on pattern recognition is a major hindrance for proper identification of inhibition mode. To address this issue, the template has been designed to facilitate the quick comparison of the non-competitive, competitive, uncompetitive, mixed non-competitive and modifier equation (Eqs 5GLYPH<21>8 & 13, Fig. 3, Supplemental Information 2, Please refer to

Figure 3 Enzyme modifier template. The enzyme modifier kinetic template (A) provides fifteen rows for substrate concentrations as well as sixteen columns for varying concentrations of enzyme modifiers, either activators or inhibitors. (B) Below the raw data, a modified direct linear plot uses the data in the no inhibitor column to generate estimates of the KM and V max while the first row of data is used to produce a linear estimate of the initial Ki value. (C) The initial kinetic values are inserted into a table which contains the parameters utilized in the fitting of each equation covered by the template. The table also contains the Sum of Squared Residuals (RSS) and the Bayesian information criterion (BIC) for assessing the fit of the model based on the provided parameters. Additionally, a box plot of the residuals is provided to offer a visual representation of the error associated with the fitting of each equation to the data.

<!-- image -->

|       |          |        |        |        |               |        |        |        | 0.0167   |
|-------|----------|--------|--------|--------|---------------|--------|--------|--------|----------|
|       | 6.666667 | 26.525 | 27.852 | 27.489 | 26.820        | 23.377 | 24.215 | 14.578 | 14.684   |
|       | 3.333333 | 27.156 |        | 27.982 |               | 22.273 | 22.304 | 10.407 | 10.194   |
|       | 1.666667 | 25.761 | 27.766 | 26.384 | 25.949        | 18.638 | 19.012 | 6.558  | 6.38     |
|       | 0.833333 | 23.735 |        | 23.757 |               |        |        | 3.886  | 3.746    |
|       |          | 20.762 | 21.474 | 19.368 | 23.119 19.525 |        | 14.677 | 2.26   | 2.22     |
|       | 0.416667 |        |        |        |               | 10.095 | 10.037 |        |          |
|       | 0.208333 | 15.383 |        | 14.238 | 14.059        | 6.401  |        | 1.269  | 1.209    |
| [S]13 |          |        |        |        |               |        |        |        |          |
|       | A        |        |        |        |               |        |        |        |          |

Vmax 2.82E+01

<!-- image -->

Full-size DOI: 10.7717/peerj.6082/fig-3

Supplemental Information 3 for step by step pictorial instructions on the use of the fitting template). To determine if the data from Biotek's application note truly does conform to the classical competitive inhibition model the data was analyzed using the modifier template (Fig. 3A). Inserting data into the template generates KM and V max values (Fig. 3B) using a modified direct linear plot. The modified direct linear plot provides a statistically robust way of determining apparent KM and V max values by providing N ( N GLYPH<0> 1) = 2 intercept values from which the median can be determined ( Cornish-Bowden, 1995 ). These median values are used as initial parameters in the fitting of the various inhibition equations. The KM and V max generated by the modified direct linear plot are in close agreement with the values reported by Held (2007) , calculated KM 0.15 mM V max 28.2 mOD/min versus reported KM 0.24 mM V max 33.4 mOD/min. Additionally, the template provides a Ki estimate based on the decrease in observable rate associated with the top substrate concentration ([S]1) and the assayed inhibitor concentrations ([I]1 to [I]7, Fig. 3A). The fit of the inhibition equations using the initial kinetic parameter is displayed both tabularly and graphically (Fig. 3C). The primary table contains the parameters employed in the fitting of each equation and values used to assess the ability of each equation to model the data. The columns containing values to evaluate the fit, namely the sum of squared residuals (RSS), relative standard error (RSE) for the regression and the Bayesian information criterion (BIC), which are color-coded such that the smallest values appear green representing the best fit and red the worst. These parameters allow evaluation of the ability of each equation to fit the observed data set with the Bayesian information criterion being included for evaluation of potential overfitting as it negatively scores fittings based on the complexity (number of parameters) of the model being used ( Burnham & Anderson, 2002 ). In this case, the number of parameter for each model is listed in the table as k. Representation of the fit of each equation is also visualized with a boxplot of the residuals, with the residuals used to generate the boxplot appear to the right of the corresponding boxplot. Ideally, a good fit would consist of an even distribution of the residual values around zero so for evaluation purposes a secondary table is presented which contain values used in the generation of the boxplot. The initial parameters produced by the template may result in fairly good fits or extremely poor fits as is apparent in the poor distribution of the residuals with the modifier equation (Fig. 3C).

To apply a global fit to the data the solver add-in for Excel is utilized ( Kemmer & Keller, 2010 ), Please refer to Supplemental Information 3 for step by step instructions on using the solver feature with the template). In fitting to the Biotek data, the solver feature was used to minimize the RSS of the fits, initially by varying parameters for the inhibition followed by all the parameters associated with the equation. For example, the fitting of the non-competitive inhibition equation was performed by minimizing the RSS through varying the Ki value, this was followed by a second minimization of the non-competitive RSS value by varying the V max, KM and Ki simultaneously.

The improvement in fit between the initial parameters generated by the template (Fig. 3C) and those present after minimizing the residuals is clear (Fig. 4, Supplemental Information 4). Both RSS and BIC values are noticeably reduced and the boxplot demonstrates a much evener distribution of the residuals around zero (Fig. 4A). The

Figure 4 Inhibition of GLYPH<12> -galactosidase by GLYPH<12> -D-thiogalactopyranoside. Global fitting of the Biotek's application note data ( Held, 2007 ) to multiple inhibitory equations. (A) In addition to producing global minimal fitting values based on the RSS, the modifier template also produces a visualization of the fitting of each inhibitory model with correlation plots of the experimental and calculated values, double reciprocal Lineweaver-Burk plots, direct plots of the reaction rate versus the substrate and Dixon plots. Shown are the global fits of the (B) Non-competitive (C) Competitive (D) Uncompetitive (E) Mixed Noncompetitive and (F) The modifier equation to the data.

<!-- image -->

Full-size DOI: 10.7717/peerj.6082/fig-4

presented values suggest that rather than GLYPH<12> -D-thiogalactopyranoside conforming to the classical competitive inhibition model a better fit can be produced using the modifier equation which assumes a hyperbolic change in KM and V max. Global fitting of the data with each equation is plotted below the boxplot (Figs. 4BGLYPH<21>4F) For each equation, the

data is presented as a correlation plot of the calculated versus the experimental data, an overlay of the model with the experimentally observed rates (v vs [S]), a double reciprocal Lineweaver-Burk plot (1/v vs 1/[S]) ( Lineweaver & Burk, 1934 ) and a Dixon plot (1/v vs [I]) ( Dixon, 1953 ; Butterworth, 1972 ). The correlation plot provides another way of visualizing the ability of each equation to fit the data as a linear regression of the observed versus the calculated values should produce a slope of 1 and a high R 2 value if the calculated values equal the observed values. For the Lineweaver-Burk plots, the lines represent the overlay of the globally fit equations rather than best fit linear regressions of the individual data sets.

An examination of the competitive plots (Fig. 4C) demonstrates the deviation of the observed data from the competitive model, where the model at higher inhibitor concentration and lower substrate concentration suggests lower rates than those observed. This problem is mirrored by the mixed non-competitive equation (Fig. 4E) which approximates the linear increase in KM produced by the competitive equation as long as the predicted GLYPH<11> Ki is significantly removed from the range of the Ki value, as is observable in the fitting ( Ki D 4.2 GLYPH<2> 10 GLYPH<0> 4 and GLYPH<11> Ki D 1.4 GLYPH<2> 10 GLYPH<0> 1 , Fig. 4A). As previously stated the modifier equation (Eq. 13) provides a better fit to the data which is apparent specifically in the low substrate, high inhibitor region of the Lineweaver-Burk plot (LWB plot Top Line Fig. 4F) and the high inhibitor region of the Dixon plot. Unfortunately, the Ki for the fit produced in Biotek's application note was not provided so a more in-depth comparison of the templates ability to fit the data cannot be undertaken.

A more thorough evaluation of the present method can be realized by studying a recent publication by Pintus et al. (2015) which describes the discovery of E. characias leaf extracts with tyrosinase inhibitory activity. The inhibitory properties of these extracts were characterized using Lineweaver-Burk plots and the data used in their analysis was made available online. To determine if the data conformed to their reported modes of inhibition, the data provided in their supplementary information was analyzed using the template. The Lineweaver-Burk plot of their aqueous extract suggested that it acted as a mixed non-competitive inhibitor. This analysis was not based on global fitting of the model to the data but rather the accepted pattern recognition associated with the position of the intercept produced by the individual best fit linear regression lines for the data produced with varying inhibitor concentrations. From the best fit linear regression lines, the Ki and GLYPH<11> Ki were reported as 0.097 and 0.33 mg/mL. Using a global fitting approach produced slightly different values (0.099 and 0.37 mg/mL) and almost halved the associated RSS value (RSS 7 GLYPH<2> 10 GLYPH<0> 4 to 4 GLYPH<2> 10 GLYPH<0> 4 Fig. 5A, Supplemental Information 5). Global fitting agreed with the reported inhibition model suggesting that only the mixed non-competitive (Fig. 5B) or modifier (Fig. 5C) equations were able to adequately model the data.

The Lineweaver-Burk plot of their ethanolic extract was reported to produce the recognizable competitive inhibition pattern where the linearly regressed best-fit lines intercepted on the Y -axis ( Pintus et al., 2015 ). However, when the data was examined using global fitting, the competitive model did not demonstrate a significantly better fit to the data when compared to the other models. When the reported Ki (23.7 m g/mL) was fixed during the global fitting process the sum of squared residuals was further worsened (RSS 0.0183 vs. 0.0143, Fig. 6A & Supplemental Information 6). Compared to the other

Figure 5 Tyrosinase inhibition by E. characias aqueous extract. Global fitting of the E. characias aqueous leave extract reported as a mixed-noncompetitive inhibitor of tyrosinase ( Pintus et al., 2015 ). (A) Fitting suggests the modifier and mixed non-competitive equations model the data significantly better than the other equations. Shown are the global fits of the (B) Mixed Non-competitive and (C) the modifier equation to the data. Full-size DOI: 10.7717/peerj.6082/fig-5

<!-- image -->

models, the only fit which was worse than the competitive model was the uncompetitive form of inhibition. Even the non-competitive model which was completely unable to model the results of the higher inhibitor concentrations was able to produce a slightly better fit according to the sum of squared residuals (Figs. 6AGLYPH<21>6C). This is a good example of the limitations associated with the competitive model, as the mandatory linear increase in KM described by the model, requires a pattern with a strict distribution of the lines in a double reciprocal Lineweaver-Burk plot rather than simply an intercept on the Y -axis. As is apparent, in the Lineweaver-Burk plot, global fitting of the competitive equation produced a relatively good fit to the data in the absence of inhibitor (lowest line in LWB plot Fig. 6C) and to the data for the enzyme in the presence of the highest concentration of inhibitor (highest line in LWB plot Fig. 6C). However, the other lines of the plot are clearly above the data points that they should be bisecting for a proper fit. For this situation, global fitting suggests that the mixed non-competitive and modifier models both provide better fits than the competitive equation (Figs. 6A, 6D, 6E).

<!-- image -->

|                | Non-competitive   | Competitive   | Uncompetitive   | Mixed Non-competitive   | Modifier equation   |
|----------------|-------------------|---------------|-----------------|-------------------------|---------------------|
| Minimum value  | 44E-02            | 18E-02        | 15E-02          | 23E-02                  | 4.33E-02            |
| quartile First |                   | 1.81E-02      |                 |                         | 7,03E-03            |
| Median value   |                   | 5.92E-03      | 2.46E-03        |                         | 9.OOE-04            |
| Third quartile | 2.64E-02          | 1.19E-02      | 4.45E-02        | 1.16E-02                |                     |
| Maximum value  |                   |               |                 | 5.67E-02                | 5.60E-02            |

<!-- image -->

Figure 6 Tyrosinase inhibition by E. characias ethanolic extract. Global fitting of the E. characias ethanolic leave extract reported as a competitive inhibitor of tyrosinase ( Pintus et al., 2015 ). (A) Fitting suggests the modifier and mixed non-competitive equations model the data better than the other equations. Shown are the global fits of the (B) Non-competitive (C) Competitive (D) Mixed Non-competitive and (E) the modifier equation to the data.

<!-- image -->

Full-size DOI: 10.7717/peerj.6082/fig-6

## PARTIAL INHIBITION EQUATIONS

The limitations of the total inhibition equations have been acknowledged through the development of partial inhibition forms for each of these equations, ie., the partial non-competitive (Eq. 14; Segel, 1975 ), partial competitive (Eq. 15; Segel, 1975 ), partial uncompetitive (Eq. 16; Bisswanger, 2002 ) and partial mixed non-competitive (Eq. 17; Yoshino, 1987 ).

v D V max GLYPH<16> [ S ] Ks GLYPH<17> C GLYPH<12> V max GLYPH<16> [ S ][ I ] KsKi GLYPH<17> GLYPH<16> 1 C GLYPH<16> [ S ] Ks GLYPH<17> C GLYPH<16> [ I ] Ki GLYPH<17> C GLYPH<16> [ S ][ I ] KsKi GLYPH<17>GLYPH<17> (14)

v D V max GLYPH<16> [ S ] Ks GLYPH<17> C GLYPH<16> [ S ] GLYPH<11> KsKi GLYPH<17> GLYPH<16> 1 C GLYPH<16> [ S ] Ks GLYPH<17> C GLYPH<16> [ I ] Ki GLYPH<17> C GLYPH<16> [ S ][ I ] GLYPH<11> KsKi GLYPH<17>GLYPH<17> (15)

v D GLYPH<16> V max C V 2[ I ] Ki GLYPH<17> [ S ] Ks C GLYPH<16> 1 C [ I ] Ki GLYPH<17> [ S ] (16)

v D V max GLYPH<18>GLYPH<18> 1 C GLYPH<18> [ I ] K 0 i GLYPH<19> .GLYPH<12> / GLYPH<19> GLYPH<16> [ S ] Ks GLYPH<17> GLYPH<19> GLYPH<18> 1 C GLYPH<18> [ I ] K 0 i GLYPH<19>GLYPH<19> 0 @ GLYPH<16> [ S ] Ks GLYPH<17> C GLYPH<18> 1 C GLYPH<18> [ I ] K 0 i GLYPH<19>GLYPH<18> K 0 s Ks GLYPH<19>GLYPH<19> GLYPH<18> 1 C GLYPH<18> [ I ] K 0 i GLYPH<19>GLYPH<19> 1 A : (17)

While there has been limited use of these equations where the raw data is accessible, Whiteley (1997) , Whiteley (1999) , Whiteley (2000) expanding on Yoshino ' ( 1987 ) work identifying forms of partial inhibition through the examination of fractional velocity plots, made the data in his papers available. The modifier template developed in the previous section also has the advantage that almost any equation can be easily inserted into the spreadsheets for global fitting analysis. This allowed the global fitting of the data presented by Whiteley (1997) , Whiteley (1999) , Whiteley (2000) to be analyzed with the total inhibition (Supplemental Information 2) and the partial inhibition equations using a version of the template modified to model the partial inhibition (Supplemental Information 7).

In Whiteleys' article examining partial competitive inhibition, data for the inhibition of glutamine synthase by alanine was presented as an example of this form of inhibition ( Whiteley, 1997 ). Inserting the data into the modifier template suggests that the data did not conform to the traditional inhibitory equations, but was modeled by the modifier equation very well (Fig. 7A, Supplemental Information 8). Fitting the data to the partial inhibition equations did indicate that partial competitive inhibition provided an even distribution of the residuals and a slightly better fit than the competitive inhibition model. However, of the partial inhibition models, the partial mixed non-competitive inhibition equation (Eq. 17) was the only model able to fit the data as well as the modifier equation (Fig. 7B, Supplemental Information 9).

In a subsequent publication on partial and complete non-competitive inhibition, Whiteley provides two examples of inhibition. The first example of inosine nucleosidase inhibition by adenine is presented as a partial non-competitive form of inhibition and the second example in which adenosine monophosphate is used to inhibit alcohol dehydrogenase is classified as non-competitive ( Whiteley, 1999 ).

Examining the first example suggests that none of the basic models fit the data as well as the modifier equation (Eq. 13; Fig. 8A; Supplemental Information 10). When examined with the partial inhibition template the partial non-competitive (Eq. 14) and partial mixed

<!-- image -->

Figure 7 Putative partial competitive inhibition. Global fitting of the data presented in Whiteleys' article on partial competitive inhibition ( Whiteley, 1997 ) to (A) the modifier equation and the classical inhibitory equations, and (B) the modifier equation and the partial inhibitory equations. Full-size DOI: 10.7717/peerj.6082/fig-7

<!-- image -->

non-competitive (Eq. 17) equations provided slightly better fits than the total inhibition models but were unable to improve on the fit provided by the modifier equation (Fig. 8B, Supplemental Information 11).

In the second example, rather than presenting as non-competitive the fitting suggested that the modifier, mixed non-competitive and partial mixed non-competitive equations all provided improved and roughly equivalent fits to the data (Figs. 8C, 8D; Supplemental Information 12, 13).

Whiteleys' most recent publication on identifying partial forms of inhibition, identifies adenosine triphosphate as a partial uncompetitive inhibitor of mevalonate diphosphate decarboxylase ( Whiteley, 2000 ). However, when globally fit to the total and partial inhibition equations, even the uncompetitive inhibition equation outperforms the partial uncompetitive equation (RSS:1.69 GLYPH<2> 10 GLYPH<0> 5 vs. 1.92 GLYPH<2> 10 GLYPH<0> 2 , Figs. 9A, 9B; Supplemental Information 14, 15). Out of all the models, the partial uncompetitive

Figure 8 Putative partial and complete non-competitive inhibition. Global fitting of the partial non-competitive data presented in Whiteleys' article on partial and complete non-competitive inhibition ( Whiteley, 1999 ) to (A) the modifier equation and the classical inhibitory equations, and (B) the modifier equation and the partial inhibitory equations. Global fitting of the non-competitive data presented in Whiteleys' article to (C) the modifier equation and the classical inhibitory equations, and (D) the modifier equation and the partial inhibitory equations.

<!-- image -->

Full-size DOI: 10.7717/peerj.6082/fig-8

<!-- image -->

Figure 9 Putative partial uncompetitive inhibition. Global fitting of the data presented in Whiteleys' article on partial uncompetitive inhibition ( Whiteley, 2000 ) to (A) the modifier equation and the classical inhibitory equations, and (B) the modifier equation and the partial inhibitory equations.

<!-- image -->

Full-size DOI: 10.7717/peerj.6082/fig-9

fared the worst while the modifier equation and the partial mixed non-competitive equation modeled the data the best (Fig. 9B).

## Overall equation fitness

A comparison of the ability of the equations to fit the examined experimental datasets suggests that the modifier equation (Eq. 13) can fit each example just as well if not better than all the other equations (Table 1, Supplemental Information 16GLYPH<21>18). Indeed, only the partial mixed non-competitive equation (Eq. 17) was comparable to the modifier equation in its ability to fit the experimental datasets. The ability of the modifier equation to outperform the other equations was further supported with simulated data (Table 2). Using simulated data for the non-competitive (Eq. 6, Supplemental Information 19, Supplemental Information 20), competitive (Eq. 5, Supplemental Information 21, 22), uncompetitive

Walsh (2018),

PeerJ

, DOI 10.7717/peerj.6082

19/24

,

6

GLYPH<21>

4

n

o

i

t

a

m

r

-

r

i

c

s

i

d

n

a

n

m

u

s ( S u p p l e m e n t a l I n f o d i n t h e l e f t -h a n d c o l t o f m i n i m u m R S S v Partial uncompetitive 2 . 4 2 E C 0 3 9 . 8 5 E GLYPH<0> 0 2 1 . 6 0 E GLYPH<0> 0 1 7 . 4 6 E GLYPH<0> 0 3 2 . 0 7 E GLYPH<0> 0 2 6 . 5 9 E GLYPH<0> 0 3 1 . 9 8 E GLYPH<0> 0 2

t

e

s

a

e

t

s

i

l

Table

| h e l i t e r a t u r e d a t o f i n h i b i t i o n i s   | n g r e e n w i t h t h               | 2 5 . 8 5 E                        | 3 5 . 0 0 E        | 2 7 . 6 3 E        | 4 3 . 2 2 E 4 5 . 4 9 E               | 6 3 . 1 6 E        | 4 1 . 7 3 E        |
|-------------------------------------------------------------|---------------------------------------|------------------------------------|--------------------|--------------------|---------------------------------------|--------------------|--------------------|
| n g o f m o d e                                             | p p e a r                             | Partial non- competitive 6 5 E C 0 | 7 6 E GLYPH<0> 0   | 3 9 E GLYPH<0> 0   | 4 1 E GLYPH<0> 0 6 2 E GLYPH<0> 0     | 7 4 E GLYPH<0> 0   | 0 1 E GLYPH<0> 0   |
| h e g l o b a l f t h e r e p o r                           | u p e r i o r f i t Modifier equation | C 0 1                              | GLYPH<0> 0 4       | GLYPH<0> 0 3       | GLYPH<0> 0 6 GLYPH<0> 0 4             | GLYPH<0> 0 6       | GLYPH<0> 0 6       |
| v a l u e s r e l a t l i t e r a t u r e d                 | c o d e d s u c h                     | E C 0 1                            | E GLYPH<0> 0 4     | E GLYPH<0> 0 3     | E GLYPH<0> 0 4 E GLYPH<0> 0 4         | E GLYPH<0> 0 6     | E GLYPH<0> 0 5     |
| equations. R S 1 7 ) ) . F o r e a c                        | v e b e e n c o l o                   | Mixed non- competitive 2 3 . 0 7   | 2 4 . 3 6          | 1 7 . 5 7          | 3 3 . 2 2 3 5 . 4 9                   | 3 3 . 1 3          | 5 1 . 6 9          |
| between GLYPH<21> ( 8 ) , ( 1 3 ) GLYPH<21>                 | d a t a s e t s h Uncompetitive       | 4 . 3 0 E C                        | 2 . 0 2 E GLYPH<0> | 1 . 6 0 E GLYPH<0> | 5 . 3 3 E GLYPH<0> 1 . 6 4 E GLYPH<0> | 1 . 9 2 E GLYPH<0> | 1 . 6 9 E GLYPH<0> |
| data fitting t e s ( E q s . ( 5                            | d e l t o f i t t Competitive         | 1 5 E C 0 1                        | 9 0 E GLYPH<0> 0 3 | 6 3 E GLYPH<0> 0 3 | 2 2 E GLYPH<0> 0 4 4 9 E GLYPH<0> 0 3 | 3 3 E GLYPH<0> 0 3 | 1 8 E GLYPH<0> 0 4 |
| of experimental s i n t h e t e m p                         | l i t y o f e a c h m                 | 0 E C 0 2                          | 0 E GLYPH<0> 0 3   | 9 E GLYPH<0> 0 2   | 3 E GLYPH<0> 0 4 4 E GLYPH<0> 0 4     | 4 E GLYPH<0> 0 6   | 6 E GLYPH<0> 0 4   |

n

o

i

t

a

u

q

e

e

h

t

h

t

i

w

)

8

1

GLYPH<21>

8

1

0

C

1

.

3

e

v

i

t

i

t

e

p

m

o

C

4

0

GLYPH<0>

9

.

3

-

n

o

n

d

e

x

i

M

3

0

GLYPH<0>

3

.

1

e

v

t

i

t

e

p

m

o

C

4

0

GLYPH<0>

6

.

8

l

a

i

t

r

a

P

4

0

GLYPH<0>

5

.

5

-

n

o

n

l

a

i

t

r

a

P

6

0

GLYPH<0>

7

.

3

-

n

o

N

5

0

GLYPH<0>

1

.

1

l

a

i

t

r

a

P

g

n

i

r

a

e

p

p

a

s

e

u

l

a

x

e

t

e

b

a

e

h

T

.

e

l

b

a

t

e

h

t

n

i

d

e

l

c

Comparison

1

.

d

e

r

n

i

Partial mixed non-

Partial competitive

Non- competitive

competitive

1

0

C

E

8

2

.

2

)

2007

Held,

(

4

0

GLYPH<0>

E

2

6

.

3

e

v

i

t

i

t

e

p

m

o

c

al.,

et

Pintus

(

)

2015

3

0

GLYPH<0>

E

7

5

.

7

al.,

et

Pintus

(

)

2015

6

0

GLYPH<0>

E

9

0

.

1

e

v

i

t

i

t

e

p

m

o

c

)

1997

Whiteley,

(

4

0

GLYPH<0>

E

2

6

.

1

e

v

i

t

i

t

e

p

m

o

c

)

1999

Whiteley,

(

6

0

GLYPH<0>

E

3

1

.

3

e

v

i

t

i

t

e

p

m

o

c

)

1999

Whiteley,

(

6

0

GLYPH<0>

E

8

9

.

1

e

v

i

t

i

t

e

p

m

o

c

n

u

)

2000

Whiteley,

(

Walsh (2018),

PeerJ

, DOI 10.7717/peerj.6082

20/24

)

8

2

GLYPH<21>

9

1

n

o

i

t

a

m

r

o

f

n

I

l

a

t

n

e

m

e

l

p

p

u

S

(

s

t

e

s

a

t

a

d

d

e

.

d

e

r

o f t h e s i m u l a t e d a t a s e t h a s a p p e a r i n g i n Partial noncompetitive 1 . 1 9 E GLYPH<0> 2 8 9 . 5 2 E C 0 1 2 . 1 7 E C 0 1 8 . 1 5 E C 0 1 6 . 2 9 E C 0 2

e

h

t

t

i

f

o

t

l

e

d

o

m

h

c

a

e

f

o

y

t

i

l

i

b

a

e

h

T

.

d

e

t

t

i

m

o

n

e

e

b

h

t

g

n

between

fitting

data

simulated

of

Comparison

2

s

e

u

Table

| t h e g l o b a l f i t t i s e d t o g e n e r a t e i m u m R S S v a l   | Modifier equation      | 2 . 0 8 E GLYPH<0> 2 8 1 . 3 3 E GLYPH<0> 0 3 6 . 1 3 E GLYPH<0> 0 8   | 7 . 2 3 E GLYPH<0> 0 8          |
|-----------------------------------------------------------------------------|------------------------|------------------------------------------------------------------------|---------------------------------|
| a t e d t o t i o n s o f m i                                               |                        | 0 7 7                                                                  | 2                               |
| s r e l e q u a t e x t                                                     | Mixed non- competitive | 5 E GLYPH<0> 1 E GLYPH<0> 0 4 E GLYPH<0> 0                             | E C 0                           |
| v a l u e t h e h t h e                                                     |                        | 8 . 5 1 . 9 1 6 . 1                                                    | 6 . 2 9                         |
| R S S a l u e o f e n w i t                                                 | Uncompetitive          |                                                                        |                                 |
| equations. T h e R S S v p e a r i n g r e                                  |                        | 5 . 8 4 E C 0 1 2 . 2 5 E C 0 2                                        | 2 . 0 8 E C 0 2 6 . 2 9 E C 0 2 |

1

(

GLYPH<21>

)

3

1

(

,

)

8

(

GLYPH<21>

)

5

(

(

s

e

t

a

l

p

m

e

t

e

h

t

n

i

s

n

o

i

t

a

u

q

e

e

h

t

h

t

i

w

i

f

r

o

i

r

e

p

u

s

t

a

h

t

h

c

u

s

d

e

d

o

c

-

r

o

l

o

c

n

e

e

b

e

v

a

h

s

t

e

s

a

t

a

d

Partial mixed non-

Partial uncompetitive

Partial competitive

Competitive

Non- competitive

competitive

8

0

GLYPH<0>

E

4

4

.

4

2

0

C

E

0

6

.

8

5

0

GLYPH<0>

E

4

5

.

1

2

0

C

E

0

1

.

3

e

v

i

t

i

t

e

p

m

o

c

-

n

o

N

1

0

GLYPH<0>

E

7

5

.

1

2

0

C

E

7

2

.

3

6

0

GLYPH<0>

E

6

2

.

2

1

0

C

E

9

5

.

9

e

v

i

t

i

t

e

p

m

o

C

7

0

GLYPH<0>

E

6

4

.

1

2

0

C

E

2

8

.

6

2

0

C

E

6

1

.

4

2

0

C

E

6

1

.

4

1

0

C

E

7

1

.

2

e

v

i

t

i

t

e

p

m

o

c

n

U

4

0

GLYPH<0>

E

2

1

.

2

2

0

C

E

0

4

.

3

4

0

GLYPH<0>

E

8

7

.

9

0

0

C

E

4

2

.

1

1

0

C

E

1

2

.

8

d

e

x

i

M

e

v

i

t

i

t

e

p

m

o

c

-

n

o

n

6

0

GLYPH<0>

E

1

8

.

1

2

0

C

E

8

8

.

2

4

0

C

E

2

7

.

4

2

0

C

E

9

2

.

6

2

0

C

E

9

2

.

6

r

e

i

f

i

d

o

M

n

o

i

t

a

u

q

e

)

n

o

i

t

a

v

i

t

c

a

(

(Eq. 7, Supplemental Information 23, 24), mixed non-competitive (Eq. 8, Supplemental Information 25, 26) equations and an example of activation generated with the modifier equation (Eq. 13, Supplemental Information 27, 28), the ability of each of the models to fit the simulated data was also examined. The simulated data contained many more data points than the experimental data used in the fittings found in Table 1. This highlighted the inability of the total inhibitor equations aside from the mixed non-competitive inhibition equation to model the data generated with the other total inhibitor models. For example, the competitive equation was unable to fit the data produced with the non-competitive equation (Table 2, RSS 3100). The modifier equation, apart from the competitive inhibition simulated data, was able to fit the other simulated data sets as well as or better than the other equations. Similarly, the partial mixed non-competitive equation also produced a good fit for the datasets and was able to fit the example of activation generated with the modifier equation (Table 2, Supplemental Information 28). This suggests the partial mixed non-competitive equation may be almost as adaptable as the modifier equation for describing a wide variety of modifier interactions. However, the modifier equation outperformed the partial mixed non-competitive equation in all the simulated datasets.

## CONCLUSIONS

Based on these examples, the modifier equation (Eq. 13) has been able to model each dataset just as well if not better than the other equations based on the sum of squared residual values. While both the inhibition of GLYPH<12> -galactosidase by GLYPH<12> -D-thiogalactopyranoside ( Held, 2007 ) and inhibition of tyrosinase with an ethanolic extract of E. characias leaves ( Pintus et al., 2015 ) were reported as examples of competitive inhibition, global fitting of their data suggested they do not conform to the classical competitive inhibition equation (Figs. 4 & 6). As none of the datasets conform to a linear change in KM , it is not surprising that the modifier equation which directly relates fractional association of modifiers with the enzyme population to change in activity fits all the examples very well.

The modifier equation defined here unifies inhibition and activation in a single equation by describing changes in V max and KM using a single binding constant (Eq. 13), something which was not described with the traditional equations such as the mixed non-competitive equation (Eq. 8). The clear distinction between inhibitor binding constants and effect on KM and V max also permits the modular expansion of the MichaelisGLYPH<21>Menten equation to accommodate multiple substrate and modifier binding interactions ( Walsh, 2012 ). This approach has already proven its value, providing valuable new insight into how the compound DAPT interacts with the multiple-substrate regulated forms of GLYPH<13> -secretase and the implications this has for amyloid precursor protein processing in Alzheimer's disease ( Walsh, 2014 ). Additionally, it has been used to provide more information on the effect drugs for Alzheimer's disease have on the multiple-substrate regulated forms of cholinesterases ( Walsh, Martin & Darvesh, 2007 ; Walsh et al., 2011b ).

New initiatives for reproducibility and openness such as the database proposed by the Standards for Reporting Enzyme Data (STRENDA) commission which will include raw data ( Tipton et al., 2014 ) suggests enzyme kinetic data will become much more transparent.

This transparency will allow easier sharing and evaluation of raw data sets, which will in turn lead to the refitting of raw data with alternative models such as the modifier equation. The global fitting templates presented here should be useful for both evaluating model suitability and in assessing whether the modifier equation described here can replace traditional approaches to inhibition and activation modeling.

## ADDITIONAL INFORMATION AND DECLARATIONS

## Funding

The authors received no funding for this work.

## Competing Interests

The authors declare there are no competing interests.

## Author Contributions

- GLYPH<15> Ryan Walsh analyzed the data, contributed analysis tools, prepared figures and/or tables, authored or reviewed drafts of the paper, approved the final draft.

## Data Availability

The following information was supplied regarding data availability:

The Supplemental Files consist of templates for analyzing enzyme kinetic data and the application of these templates to previously published data and simulated datasets.

## Supplemental Information

Supplemental information for this article can be found online at http://dx.doi.org/10.7717/ peerj.6082#supplemental-information.

## REFERENCES

Baici A. 2015. Kinetics of enzyme-modifier interactions . Vienna: Springer-Verlag Wien.

Bernett MJ, Blaber SI, Scarisbrick IA, Dhanarajan P, Thompson SM, Blaber M. 2002. Crystal structure and biochemical characterization of human kallikrein 6 reveals that a trypsin-like kallikrein is expressed in the central nervous system. The Journal of Biological Chemistry 277 :24562GLYPH<21>24570 DOI 10.1074/jbc.M202392200.

Bisswanger H. 2002. Enzyme kinetics: principles and methods . Second Edition. Weinheim: WILEY-VCH Verlag GmbH DOI 10.1002/9783527622023.

Brandt RB, Laux JE, Yates SW. 1987. Calculation of inhibitor Ki and inhibitor type from the concentration of inhibitor for 50% inhibition for MichaelisGLYPH<21> Menten enzymes. Biochemical Medicine and Metabolic Biology 37 :344GLYPH<21>349 DOI 10.1016/0885-4505(87)90046-6.

Burnham KP, Anderson DR. 2002. Model selection and multimodel inference: a practical Q3 information-theoretic approach . New York: Springer-Verlag.

Butterworth PJ. 1972. The use of Dixon plots to study enzyme inhibition. Biochimica et Biophysica Acta/General Subjects 289 :251GLYPH<21>253.

Cleland WW. 1970. Steady state kinetics. In: Boyer PD, ed. The enzymes . 3rd Edition. New York: Academic Press.

Cornish-Bowden A. 1995. Fundamentals of enzyme kinetics . 2nd Edition. London: Portland Press.

Dixon M. 1953. The determination of enzyme inhibitor constants. Biochemical Journal 55 :170GLYPH<21>171 DOI 10.1042/bj0550170.

Fontes R, Ribeiro JM, Sillero A. 2000. Inhibition and activation of enzymes. The effect of a modifier on the reaction rate and on kinetic parameters. Acta Biochimica Polonica 47 :233GLYPH<21>257.

- Gesztelyi R, Zsuga J, Kemeny-Beke A, Varga B, Juhasz B, Tosaki A. 2012. The Hill equation and the origin of quantitative pharmacology. Archive for History of Exact Sciences 66 :427GLYPH<21>438 DOI 10.1007/s00407-012-0098-5.
- Held P. 2007. Kinetic analysis of GLYPH<12> -galactosidase activity using the PowerWave TM HT and Gen5 TM data analysis software. Winooski: BioTek Instruments.

Kemmer G, Keller S. 2010. Nonlinear least-squares data fitting in Excel spreadsheets. Nature Protocols 5 :267GLYPH<21>281 DOI 10.1038/nprot.2009.182.

Lazareno S, Birdsall NJ. 1993. Estimation of competitive antagonist affinity from functional inhibition curves using the Gaddum, Schild and Cheng-Prusoff equations. British Journal of Pharmacology 109 :1110GLYPH<21>1119

DOI 10.1111/j.1476-5381.1993.tb13737.x.

Lineweaver H, Burk D. 1934. The determination of enzyme dissociation constants. Journal of the American Chemical Society 56 :658GLYPH<21>666 DOI 10.1021/ja01318a036.

- McElroy WD. 1947. The mechanism of inhibition of cellular activity by narcotics. The Quarterly Review of Biology 22 :25GLYPH<21>58 DOI 10.1086/395578.
- Michaelis L, Menten ML. 1913. Die Kinetik der Invertinwirkung. Biochemische Zeitschrift 49 :333GLYPH<21>369.
- Pintus F, SpanGLYPH<242> D, Corona A, Medda R. 2015. Antityrosinase activity of Euphorbia characias extracts. PeerJ 3 :e1305 DOI 10.7717/peerj.1305.
- Sebaugh JL. 2011. Guidelines for accurate EC50/IC50 estimation. Pharmaceutical Statistics 10 :128GLYPH<21>134 DOI 10.1002/pst.426.
- Segel IH. 1975. Enzyme kinetics: behavior and analysis of rapid equilibrium and steady-state enzyme systems . New York: John Wiley & Sons.

Sousa MO, Miranda TL, Costa EB, Bittar ER, Santoro MM, Figueiredo AF. 2001. Linear competitive inhibition of human tissue kallikrein by 4-aminobenzamidine and benzamidine and linear mixed inhibition by 4-nitroaniline and aniline. Brazilian Journal of Medical and Biological Research 34 :35GLYPH<21>44 DOI 10.1590/S0100-879X2001000100004.

Tipton KF, Armstrong RN, Bakker BM, Bairoch A, Cornish-Bowden A, Halling PJ, Hofmeyr J-HS, Leyh TS, Kettner C, Raushel FM, Rohwer J, Schomburg D, Steinbeck C. 2014. Standards for reporting enzyme data: the STRENDA consortium: what it aims to do and why it should be helpful. Perspectives in Science 1 :131GLYPH<21>137 DOI 10.1016/j.pisc.2014.02.012.

Walsh R. 2012. Alternative perspectives of enzyme kinetic modeling. In: Ekinci D, ed. Medicinal chemistry and drug design . London: InTech, 357GLYPH<21>372 DOI 10.5772/36973.

- Walsh R. 2014. Are improper kinetic models hampering drug development? PeerJ 2 :e649 DOI 10.7717/peerj.649.
- Walsh R, Martin E, Darvesh S. 2007. A versatile equation to describe reversible enzyme inhibition and activation kinetics: modeling beta-galactosidase and butyrylcholinesterase. Biochimica et Biophysica Acta 1770 :733GLYPH<21>746 DOI 10.1016/j.bbagen.2007.01.001.
- Walsh R, Martin E, Darvesh S. 2011a. Limitations of conventional inhibitor classifications. Integrative Biology 3 :1197GLYPH<21>1201 DOI 10.1039/c1ib00053e.
- Walsh R, Rockwood K, Martin E, Darvesh S. 2011b. Synergistic inhibition of butyrylcholinesterase by galantamine and citalopram. Biochimica et Biophysica Acta 1810 :1230GLYPH<21>1235 DOI 10.1016/j.bbagen.2011.08.010.
- Whiteley CG. 1997. Enzyme kinetics: partial and complete competitive inhibition. Biochemical Education 25 :144GLYPH<21>146 DOI 10.1016/S0307-4412(97)00070-8.
- Whiteley CG. 1999. Enzyme kinetics: partial and complete non-competitive inhibition. Biochemical Education 27 :15GLYPH<21>18 DOI 10.1016/S0307-4412(98)00265-9.
- Whiteley CG. 2000. Enzyme kinetics: partial and complete uncompetitive inhibition. Biochemical Education 28 :144GLYPH<21>147 DOI 10.1111/j.1539-3429.2000.tb00050.x.

Yoshino M. 1987. A graphical method for determining inhibition parameters for partial and complete inhibitors. Biochemical Journal 248 :815GLYPH<21>820 DOI 10.1042/bj2480815.