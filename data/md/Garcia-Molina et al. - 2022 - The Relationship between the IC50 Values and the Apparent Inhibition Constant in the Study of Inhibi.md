<!-- image -->

<!-- image -->

Article

## The Relationship between the IC 50 Values and the Apparent Inhibition Constant in the Study of Inhibitors of Tyrosinase Diphenolase Activity Helps Confirm the Mechanism of Inhibition

Pablo Garcia-Molina 1 , Francisco Garcia-Molina 2, * , Jose Antonio Teruel-Puche 3 , Jose Neptuno Rodriguez-Lopez 1 , Francisco Garcia-Canovas 1 and Jose Luis Muñoz-Muñoz 4, *

- 1 GENZ-Group of Research on Enzymology, Department of Biochemistry and Molecular Biology-A, Regional Campus of International Excellence 'Campus Mare Nostrum', University of Murcia, Espinardo,
- 30100 Murcia, Spain; pablo.garcia14@um.es (P.G.-M.); neptuno@um.es (J.N.R.-L.); canovasf@um.es (F.G.-C.)
- 2 Department of Anatom í a Patol ó gica, Hospital General Universitario Reina Sof í a, Av. Intendente Jorge Palacios, 1, 30003 Murcia, Spain
- 3 Department of Biochemistry and Molecular Biology-A, Regional Campus of International Excellence 'Campus Mare Nostrum', University of Murcia, Espinardo, 30100 Murcia, Spain; teruel@um.es
- 4 Microbial Enzymology Lab, Department of Applied Sciences, Ellison Building A, University of Northumbria, Newcastle Upon Tyne NE1 8ST, UK
- * Correspondence: pacogm@um.es (F.G.-M.); jose.munoz@northumbria.ac.uk (J.L.M.-M.)

Abstract: Tyrosinase is the enzyme involved in melanization and is also responsible for the browning of fruits and vegetables. Control of its activity can be carried out using inhibitors, which is interesting in terms of quantitatively understanding the action of these regulators. In the study of the inhibition of the diphenolase activity of tyrosinase, it is intriguing to know the strength and type of inhibition. The strength is indicated by the value of the inhibition constant(s), and the type can be, in a first approximation: competitive, non-competitive, uncompetitive and mixed. In this work, it is proposed to calculate the degree of inhibition ( i D ), varying the concentration of inhibitor to a fixed concentration of substrate, L-dopa (D). The non-linear regression adjustment of i D with respect to the initial inhibitor concentration [ I ] 0 allows for the calculation of the inhibitor concentration necessary to inhibit the activity by 50%, at a given substrate concentration (IC 50 ), thus avoiding making interpolations between different values of i D . The analytical expression of the IC 50 , for the different types of inhibition, are related to the apparent inhibition constant (K app I ) . Therefore, this parameter can be used: (a) To classify a series of inhibitors of an enzyme by their power. Determining these values at a fixed substrate concentration, the lower IC 50 , the more potent the inhibitor. (b) Checking an inhibitor for which the type and the inhibition constant have been determined (using the usual methods), must confirm the IC 50 value according to the corresponding analytical expression. (c) The type and strength of an inhibitor can be analysed from the study of the variation in i D and IC 50 with substrate concentration. The dependence of IC 50 on the substrate concentration allows us to distinguish between non-competitive inhibition ( i D does not depend on [ D ] 0 ) and the rest. In the case of competitive inhibition, this dependence of i D on [ D ] 0 leads to an ambiguity between competitive inhibition and type 1 mixed inhibition. This is solved by adjusting the data to the possible equations; in the case of a competitive inhibitor, the calculation of K app I1 is carried out from the IC 50 expression. The same occurs with uncompetitive inhibition and type 2 mixed inhibition. The representation of i D vs. n, with n = [ D ] 0 /K D m , allows us to distinguish between them. A hyperbolic i D vs. n representation that passes through the origin of coordinates is a characteristic of uncompetitive inhibition; the calculation of K app I2 is immediate from the IC 50 value. In the case of mixed inhibitors, the values of the apparent inhibition constant of meta-tyrosinase (Em) and oxy-tyrosinase (Eox), K app I1 and the apparent inhibition constant of metatyrosinase/Dopa complexes (EmD) and oxytyrosinase/Dopa (EoxD), K app I2 are obtained from the dependence of i D vs. n, and the results obtained must comply with the IC 50 value.

<!-- image -->

Citation: Garcia-Molina, P.; Garcia-Molina, F.; Teruel-Puche, J.A.; Rodriguez-Lopez, J.N.; GarciaCanovas, F.; Muñoz-Muñoz, J.L. The Relationship between the IC50 Values and the Apparent Inhibition Constant in the Study of Inhibitors of Tyrosinase Diphenolase Activity Helps Confirm the Mechanism of Inhibition. Molecules 2022 , 27 , 3141. https://doi.org/ 10.3390/molecules27103141

Academic Editor: Marko Goliˆcnik

Received: 9 April 2022

Accepted: 11 May 2022

Published: 13 May 2022

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

<!-- image -->

Copyright: © 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ 4.0/).

, x FOR PEER REVIEW

Keywords: tyrosinase; polyphenol oxidase; diphenolase activity; IC 50 ; inhibition; K app I Keywords: tyrosinase; polyphenol oxidase; diphenolase activity; IC50; inhibition; K ୍ ୟ୮୮

## 1. Introduction 1. Introduction

Tyrosinase (EC 1.14.18.1) is an enzyme widely distributed in nature, including in bacteria, fungi, plants and animals [1]. The enzyme catalyses the rate-limiting step in melanin biosynthesis in mammals, the conversion of L-tyrosine to L-dopa and the oxidation of the latter to Lo -dopaquinone [2] (Scheme 1). The abnormal functioning of tyrosinase causes hyperpigmentation or hypopigmentation phenomena [3,4]. Tyrosinase (EC 1.14.18.1) is an enzyme widely distributed in nature, including in bacteria, fungi, plants and animals [1]. The enzyme catalyses the rate-limiting step in melanin biosynthesis in mammals, the conversion of L-tyrosine to L-dopa and the oxidation of the latter to Lo -dopaquinone [2] (Scheme 1). The abnormal functioning of tyrosinase causes hyperpigmentation or hypopigmentation phenomena [3,4].

<!-- image -->

Scheme 1. Melanin biosynthesis pathway. M, monophenol (L-tyrosine); D, o -diphenol (L-dopa); DQ, (Lo -dopaquinone); L, leucodopachrome and DC, L-dopachrome. Scheme 1. Melanin biosynthesis pathway. M, monophenol (L-tyrosine); D, o -diphenol (L-dopa); DQ, (Lo -dopaquinone); L, leucodopachrome and DC, L-dopachrome.

There is great interest in the control of tyrosinase activity, especially through the use of inhibitors, which can be natural or synthetic [5-11]. This enzyme has two activities: firstly, monophenolase activity, catalysing the passage from L-tyrosine to L-dopa, and secondly, diphenolase activity, which catalyses the passage from L-dopa to Lodopaquinone [1,2]. Monophenolase activity exhibits a lag period 𝜏 before reaching steady state [12]. For this reason, the study of inhibitors on this activity of the enzyme is difficult and it is best to eliminate the delay period by adding a certain amount of L-dopa, necessary to reach the steady state. Once this addition is made, tyrosinase behaves kinetically as a Michaelian enzyme [13]. There is great interest in the control of tyrosinase activity, especially through the use of inhibitors, which can be natural or synthetic [5-11]. This enzyme has two activities: firstly, monophenolase activity, catalysing the passage from L-tyrosine to L-dopa, and secondly, diphenolase activity, which catalyses the passage from L-dopa to Lo -dopaquinone [1,2]. Monophenolase activity exhibits a lag period t before reaching steady state [12]. For this reason, the study of inhibitors on this activity of the enzyme is difficult and it is best to eliminate the delay period by adding a certain amount of L-dopa, necessary to reach the steady state. Once this addition is made, tyrosinase behaves kinetically as a Michaelian enzyme [13].

50 ୍ The diagnostic value of the reversible enzymatic inhibition of the IC 50 parameter and its relationship with K ୍ ୟ୮୮ has been described for some time [16]. In the case of a monosubstrate reaction and under fast equilibrium conditions, the relationship between IC 50 and K ୍ ୟ୮୮ (competitive, non-competitive and uncompetitive inhibitors) has been established. In these analytical expressions, the dependence of 𝑖 ୈ (degree of inhibition of diphenolase activity) on concentration of substrate on which the experiments are performed is revealed, except in the case of non-competitive inhibition [16]. An analysis of data, based on the plots of 1/IC ହ଴ vs. V ଴ V ୫ୟ୶ / , the unihibited rate ( V ଴ ) divided by the maximal rate ( V ୫ୟ୶ ), was proposed [17]. Subsequently, making use of the dependence of the inhibition degree on the ratio of the substrate concentration, ሾSሿ ଴ , to the Michaelis constant ( K ୫ ୗ ), ሾSሿ ଴ K ୫ ୗ / discrimination was addressed between mechanisms, considering a monosubstrate reaction in rapid equilibrium [18]. Experimental design and data analysis based The diagnostic value of the reversible enzymatic inhibition of the IC 50 parameter and its relationship with K app I has been described for some time [16]. In the case of a monosubstrate reaction and under fast equilibrium conditions, the relationship between IC 50 and K app I (competitive, non-competitive and uncompetitive inhibitors) has been established. In these analytical expressions, the dependence of i D (degree of inhibition of diphenolase activity) on concentration of substrate on which the experiments are performed is revealed, except in the case of non-competitive inhibition [16]. An analysis of data, based on the plots of 1/IC 50 vs. V 0 /Vmax, the unihibited rate (V 0 ) divided by the maximal rate (Vmax), was proposed [17]. Subsequently, making use of the dependence of the inhibition degree on the ratio of the substrate concentration, [ S ] 0 , to the Michaelis constant (K S m ), [ S ] 0 /K S m discrimination was addressed between mechanisms, considering a monosubstrate reaction in rapid equilibrium [18]. Experimental design and data analysis based on the dependence of IC 50 vs. [ S ] 0 /Km has recently been proposed [19].

Diphenolase activity is of the Michaelian type and is normally used to study the kinetics of inhibitors, characterizing the type of inhibition and the strength of the inhibitor [13]. In addition, a parameter is calculated, the IC 50 , which indicates the concentration of inhibitor that causes 50% inhibition under certain experimental conditions [14,15]. This IC parameter is related to the value of the apparent inhibition constant, K ୟ୮୮ [16]. Diphenolase activity is of the Michaelian type and is normally used to study the kinetics of inhibitors, characterizing the type of inhibition and the strength of the inhibitor [13]. In addition, a parameter is calculated, the IC 50 , which indicates the concentration of inhibitor that causes 50% inhibition under certain experimental conditions [14,15]. This IC 50 parameter is related to the value of the apparent inhibition constant, K app I [16].

on the dependence of IC 50 vs. ሾSሿ ଴ K ୫ / has recently been proposed [19]. Since tyrosinase inhibitors can control the activity of the enzyme, their study is very important. Thus, in mammalian pigmentation, an excessive action of tyrosinase causes hyperpigmentation, such as melasma, freckles and ephelides. In addition, the enzyme is Since tyrosinase inhibitors can control the activity of the enzyme, their study is very important. Thus, in mammalian pigmentation, an excessive action of tyrosinase causes hyperpigmentation, such as melasma, freckles and ephelides. In addition, the enzyme is responsible for the browning of fruits, vegetables, fungi and crustaceans, which leads to a

responsible for the browning of fruits, vegetables, fungi and crustaceans, which leads to

Molecules

2022

,

27

, x FOR PEER REVIEW

3 of 22

Molecules

2022

,

27

, x FOR PEER REVIEW

3 of 22

a decrease in commercial value. For these reasons, we focus our study on the quantitative

a decrease in commercial value. For these reasons, we focus our study on the quantitative

characterization of the inhibitors. The purpose of this work is to establish quantitative

decrease in commercial value. For these reasons, we focus our study on the quantitative characterization of the inhibitors. The purpose of this work is to establish quantitative relationships between i D and the inhibitor concentration [ I ] 0 at a fixed substrate concentration, and with the relationship [ D ] 0 /Km = n at a fixed concentration of inhibitor, where [ D ] 0 is the initial concentration of L-dopa, for the diphenolase activity of tyrosinase. From these data it is possible to determine, from the dependence of i D vs. [ I ] 0 , the value of IC 50 . This value should make it possible to: (a) Order different inhibitors by their inhibitory power, where for a lower IC 50 , the more powerful the inhibitor is; (b) Check an inhibitor studied via the usual methods (1/V 0, i vs. 1/ [ D ] 0 at different concentrations of [ I ] 0 ) whose type and strength are known (K app I ). It must be confirmed that the analytical expression of the IC 50 corresponding to this type of inhibition is fulfilled; (c) Analyse the variation in i D and IC 50 value with respect to the substrate concentration. If when the value of [ D ] 0 varies, i D does not vary, the inhibition is non-competitive and the value of K app I is equal to the value of IC 50 . In other cases, to determine the type and strength of the inhibitor, the variation of i D vs. [ D ] 0 must be studied. The experimental results obtained must comply with the analytical expressions deduced for IC 50 . In turn, this confirms the validity of the kinetic study carried out. characterization of the inhibitors. The purpose of this work is to establish quantitative relationships between 𝑖 ୈ and the inhibitor concentration ሾIሿ ଴ at a fixed substrate concentration, and with the relationship ሾDሿ ଴ K ୫ = n / at a fixed concentration of inhibitor, where ሾDሿ ଴ is the initial concentration of L-dopa, for the diphenolase activity of tyrosinase. From these data it is possible to determine, from the dependence of 𝑖 ୈ vs. ሾIሿ ଴ , the value of IC 50 . This value should make it possible to: (a) Order different inhibitors by their inhibitory power, where for a lower IC 50 , the more powerful the inhibitor is; (b) Check an inhibitor studied via the usual methods ( 1 V ଴,୧ / vs. 1 ሾDሿ ଴ / at different concentrations of ሾIሿ ଴ ) whose type and strength are known ( K ୍ ୟ୮୮ ). It must be confirmed that the analytical expression of the IC 50 corresponding to this type of inhibition is fulfilled; (c) Analyse the variation in 𝑖 ୈ and IC 50 value with respect to the substrate concentration. If when the value of ሾDሿ ଴ varies, 𝑖 ୈ does not vary, the inhibition is non-competitive and the value of K ୍ ୟ୮୮ is equal to the value of IC 50 . In other cases, to determine the type and strength of the inhibitor, the variation of 𝑖 ୈ vs. ሾDሿ ଴ must be studied. The experimental results obtained must comply with the analytical expressions deduced for IC 50 . In turn, this confirms the validity of the kinetic study carried out. relationships between 𝑖 ୈ and the inhibitor concentration ሾIሿ ଴ at a fixed substrate concentration, and with the relationship ሾDሿ ଴ K ୫ = n / at a fixed concentration of inhibitor, where ሾDሿ ଴ is the initial concentration of L-dopa, for the diphenolase activity of tyrosinase. From these data it is possible to determine, from the dependence of 𝑖 ୈ vs. ሾIሿ ଴ , the value of IC 50 . This value should make it possible to: (a) Order different inhibitors by their inhibitory power, where for a lower IC 50 , the more powerful the inhibitor is; (b) Check an inhibitor studied via the usual methods ( 1 V ଴,୧ / vs. 1 ሾDሿ ଴ / at different concentrations of ሾIሿ ଴ ) whose type and strength are known ( K ୍ ୟ୮୮ ). It must be confirmed that the analytical expression of the IC 50 corresponding to this type of inhibition is fulfilled; (c) Analyse the variation in 𝑖 ୈ and IC 50 value with respect to the substrate concentration. If when the value of ሾDሿ ଴ varies, 𝑖 ୈ does not vary, the inhibition is non-competitive and the value of K ୍ ୟ୮୮ is equal to the value of IC 50 . In other cases, to determine the type and strength of the inhibitor, the variation of 𝑖 ୈ vs. ሾDሿ ଴ must be studied. The experimental results obtained must comply with the analytical expressions deduced for IC 50 . In turn, this confirms the validity of the kinetic study carried out. 2. Results and Discussion

## 2. Results and Discussion 2. Results and Discussion 2.1. Diphenolase Activity

## 2.1. Diphenolase Activity 2.1. Diphenolase Activity Tyrosinase catalyses the hydroxylation of monophenols to

o

-diphenols (monopheno-

Tyrosinase catalyses the hydroxylation of monophenols to o -diphenols (monophenolase activity) and the oxidation of o -diphenols to o -quinones (diphenolase activity). Tyrosinase catalyses the hydroxylation of monophenols to o -diphenols (monophenolase activity) and the oxidation of o -diphenols to o -quinones (diphenolase activity). In the case of tyrosinase diphenolase activity, the mechanism is in Scheme 2 [20]: lase activity) and the oxidation of o -diphenols to o -quinones (diphenolase activity). In the case of tyrosinase diphenolase activity, the mechanism is in Scheme 2 [20]:

In the case of tyrosinase diphenolase activity, the mechanism is in Scheme 2 [20]:

<!-- image -->

Scheme 2. Diphenolase activity of tyrosinase. Em, met-tyrosinase; Ed, deoxy-tyrosinase; Eox, oxytyrosinase; D, L-dopa; DQ, Lo -dopaquinone-H+ (in the amine group) and DC, L-dopachrome. Scheme 2. Diphenolase activity of tyrosinase. Em, met-tyrosinase; Ed, deoxy-tyrosinase; Eox, oxytyrosinase; D, L-dopa; DQ, Lo -dopaquinone-H+ (in the amine group) and DC, L-dopachrome. Scheme 2. Diphenolase activity of tyrosinase. Em, met-tyrosinase; Ed, deoxy-tyrosinase; Eox, oxytyrosinase; D, L-dopa; DQ, Lo -dopaquinone-H+ (in the amine group) and DC, L-dopachrome.

The general case of the inhibition of this activity can be expressed according to Scheme 3: The general case of the inhibition of this activity can be expressed according to Scheme 3: The general case of the inhibition of this activity can be expressed according to Scheme 3:

Scheme 3. Generalized inhibition of tyrosinase diphenolase activity. Scheme 3. Generalized inhibition of tyrosinase diphenolase activity.

<!-- image -->

Scheme 3.

Generalized inhibition of tyrosinase diphenolase activity.

From  the  mechanism  described  in  Scheme  3,  different  particular  cases  can  be

considered:  competitive  inhibition,  where  the  inhibitor  binds  preferentially  to  the

enzymatic forms Em and Eox in such a way that

4 of 22 ; non-competitive inhibition,

K

ୟ୮୮

୍

మ

→∞

where the inhibitor binds to the free enzymatic forms (Em and Eox) and to the complexes

(EmD and EoxD), fulfilling

glyph[negationslash]

ୟ୮୮

୍

ୟ୮୮

୍

From the mechanism described in Scheme 3, different particular cases can be considered: competitive inhibition, where the inhibitor binds preferentially to the enzymatic forms Em and Eox in such a way that K app I 2 → ¥ ; non-competitive inhibition, where the inhibitor binds to the free enzymatic forms (Em and Eox) and to the complexes (EmD and EoxD), fulfilling K app I 1 ∼ = K app I 2 ; uncompetitive inhibitors bind preferentially to the EmD complexes and EoxD such that K app I 1 → ¥ ; finally, in the mixed inhibition, it is true that K app I 1 = K app I 2 (the expressions of K app I 1 and K app I 2 are described in the Supplementary Material, Equations (S9) and (S10)). Note that these constants are apparent since their analytical expressions include substrate catalysis rate constants and inhibition equilibrium constants. భ మ the EmD complexes and EoxD such that K ୍ భ ୟ୮୮ →∞ ; finally, in the mixed inhibition, it is true  that K ୍ భ ୟ୮୮ ≠ K ୍ మ ୟ୮୮ (the  expressions  of K ୍ భ ୟ୮୮ and K ୍ మ ୟ୮୮ are  described  in  the Supplementary Material, Equations (S9) and (S10)). Note that these constants are apparent since their analytical expressions include substrate catalysis rate constants and inhibition equilibrium constants. The affinity of the enzyme for oxygen is so great [21,22] that at the concentration of oxygen  in  the  solution  it  is  saturated,  and  therefore  the  inhibitor  does  not  bind  to deoxytyrosinase (Ed) K ଵଷ →∞ .

The affinity of the enzyme for oxygen is so great [21,22] that at the concentration of oxygen in the solution it is saturated, and therefore the inhibitor does not bind to deoxytyrosinase (Ed) K 13 → ¥ . 2.2. Tyrosinase Inhibition by Benzoate and Cinnamate The inhibition of tyrosinase with benzoate and cinnamate has been studied. Working

experimentally at a fixed inhibitor concentration and varying the substrate concentration,

/

1 V

vs.

/

1 ሾDሿ

gives a straight

The inhibition of tyrosinase with benzoate and cinnamate has been studied. Working experimentally at a fixed inhibitor concentration and varying the substrate concentration, the initial velocities (V D,DC o,i ) and the representation of 1/V D,DC o,i vs. 1/ [ D ] 0 gives a straight line. This approach is repeated at various inhibitor concentrations (the lines intersect at the 1/V D,DC o,i axis) and K app m is then determined at each inhibitor concentration [13]. A secondary plot of K app m vs. [ I ] 0 allows for determination of the apparent inhibition constant K app I [23-25]. The application of this methodology allows us to determine the type of inhibition and the strength of these inhibitors, meaning in this case that these compounds behave as competitive inhibitors, being benzoate and cinnamate at pH = 7.0, with K app I values of 0.53 ± 0.06 mM (benzoate) and 0.44 ± 0.04 mM (cinnamate). ୭,୧ ୭,୧ ଴ line. This approach is repeated at various inhibitor concentrations (the lines intersect at the 1 V ୭,୧ ୈ,ୈେ / axis)  and K ୫ ୟ୮୮ is then determined at each inhibitor concentration [13]. A secondary plot of K ୫ ୟ୮୮ vs.  ሾIሿ ଴ allows for determination of the apparent inhibition constant K ୍ ୟ୮୮ [23-25]. The application of this methodology allows us to determine the type of inhibition and the strength of these inhibitors, meaning in this case that these compounds behave as competitive inhibitors, being benzoate and cinnamate at pH = 7.0, with K ୍ ୟ୮୮ values of 0.53 ± 0.06 mM (benzoate) and 0.44 ± 0.04 mM (cinnamate). Check of Inhibition by Cinnamate and Benzoate. Calculation of the IC 50 Value and Its Relationship with K ୟ୮୮

## 2.2. Tyrosinase Inhibition by Benzoate and Cinnamate the initial velocities ( V ୈ,ୈେ ) and the representation of

୍

Check of Inhibition by Cinnamate and Benzoate. Calculation of the IC 50 Value and Its Relationship with K app I In this work, the experimental values of 𝑖 ୈ have been calculated at a fixed concentration of substrate, ሾDሿ ଴ = K ୫ ୈ and different concentrations of inhibitor, both in the pres-

In this work, the experimental values of i D have been calculated at a fixed concentration of substrate, [ D ] 0 = K D m and different concentrations of inhibitor, both in the presence of benzoate and in the presence of cinnamate. Adjusting the values of i D to Equation (S16), the IC 50 values shown in Figure 1, IC B 50 for benzoate and IC C 50 for cinnamate are obtained. ence of benzoate and in the presence of cinnamate. Adjusting the values of 𝑖 ୈ to Equation (S16), the IC 50 values shown in Figure 1, IC ହ଴ ୆ for benzoate and IC ହ଴ େ for cinnamate are obtained.

Figure 1. Representation of the 𝑖 ୈ (degree of inhibition of diphenolase activity) values, calculated from the experimental values of V ଴ ୈ,ୈେ (initial rate of dopachrome accumulation when the enzyme Figure 1. Representation of the i D (degree of inhibition of diphenolase activity) values, calculated from the experimental values of V D,DC 0 (initial rate of dopachrome accumulation when the enzyme acts on L-dopa) and V D,DC o,i (initial rate of dopachrome accumulation when the enzyme acts on L-dopa in the presence of inhibitor), with respect to the inhibitor concentration. ( A ). Representation of i D for

<!-- image -->

ୈ,ୈେ

K

≅ K

; uncompetitive inhibitors bind preferentially to

Figure 2. Chemical structures: Benzoate ( A ), cinnamate ( B ), and their derivatives ( a , b Figure 2. Chemical structures: Benzoate ( A ), cinnamate ( B ), and their derivatives ( a , b ).

<!-- image -->

acts on L-dopa) and

V

ୈ,ୈେ

୭,୧

(initial rate of dopachrome accumulation when the enzyme acts on L-

dopa in the presence of inhibitor), with respect to the inhibitor concentration. (

A

). Representation

of

𝑖

ୈ

for benzoate. The experimental conditions were:

ሾEሿ

଴

= 5 nM

ሾDሿ

଴

= 0.5 mM

, phosphate

buffer pH = 7, 25 °C and the inhibitor concentration (benzoate) was varied (mM): 0, 0.1, 0.3, 0.7, 1,

1.2, 1.4 and 1.7. (

B

). Representation of the

𝑖

ୈ

values for cinnamate. The experimental conditions

were the same as in Figure 1A and the inhibitor concentration (cinnamate) was varied according to

benzoate. The experimental conditions were: [ E ] 0 = 5 nM [ D ] 0 = 0.5 mM, phosphate buffer pH = 7, 25 · C and the inhibitor concentration (benzoate) was varied (mM): 0, 0.1, 0.3, 0.7, 1, 1.2, 1.4 and 1.7. ( B ). Representation of the i D values for cinnamate. The experimental conditions were the same as in Figure 1A and the inhibitor concentration (cinnamate) was varied according to (mM): 0, 0.1, 0.3, 0.6, 1, 1.4, 1.5 and 1.7. (mM): 0, 0.1, 0.3, 0.6, 1, 1.4, 1.5 and 1.7. With the values of IC ହ଴ ୆ = 0.99 ± 0.02 mM and IC ହ଴ େ = 0.80 ± 0.02 mM obtained for benzoate and cinnamate, respectively, so being IC ହ଴ େ < IC ହ଴ ୆ , then cinnamate is a more potent inhibitor than benzoate. The values of K ୍ ୟ୮୮ (Equation (S20)) are calculated and comୟ୮୮

With the values of IC B 50 = 0.99 ± 0.02 mM and IC C 50 = 0.80 ± 0.02 mM obtained for benzoate and cinnamate, respectively, so being IC C 50 < IC B 50 , then cinnamate is a more potent inhibitor than benzoate. The values of K app I (Equation (S20)) are calculated and compared with the values obtained from K app I following the experimental method described above for competitive inhibitors (see Table 1) [13]. Note the similarity between the values obtained by the two methods. The chemical structures of benzoate and cinnamate are shown in Figure 2. The docking of these compounds to met-tyrosinase and oxy-tyrosinase is shown in Figures 3 and 4. The values of the dissociation constants are shown in Table 2. Note that at the working pH, these compounds are as benzoate and cinnamate and therefore bind better to met-tyrosinase than to oxy-tyrosinase, as shown in Figures 3 and 4. The K D value is higher for the case of oxy-tyrosinase (Table 2) due to the repulsion between the negative charges of the compounds and the peroxide of oxy-tyrosinase. pared with the values obtained from K ୍ following the experimental method described above for competitive inhibitors (see Table 1) [13]. Note the similarity between the values obtained by the two methods. The chemical structures of benzoate and cinnamate are shown in Figure 2. The docking of these compounds to met-tyrosinase and oxy-tyrosinase is shown in Figures 3 and 4. The values of the dissociation constants are shown in Table 2. Note that at the working pH, these compounds are as benzoate and cinnamate and therefore bind better to met-tyrosinase than to oxy-tyrosinase, as shown in Figures 3 and 4. The K D value is higher for the case of oxy-tyrosinase (Table 2) due to the repulsion between the negative charges of the compounds and the peroxide of oxy-tyrosinase. Table 1. Apparent inhibition constants ( K ୍ ୟ୮୮ ) obtained for benzoate and cinnamate for the diphenolase activity of tyrosinase on L-dopa. (a) K ୍ ୟ୮୮ values obtained from the value obtained from IC50 and (b) obtained through the experimental design of a competitive inhibitor.

𝐚𝐩𝐩

𝐚𝐩𝐩

ହ଴

Table 1. Apparent inhibition constants (K app I ) obtained for benzoate and cinnamate for the diphenolase activity of tyrosinase on L-dopa. (a) K app I values obtained from the value obtained from IC 50 and (b) obtained through the experimental design of a competitive inhibitor. Inhibitor (a) 𝐊 𝐈 (mM) (b) 𝐊 𝐈 (mM) Benzoate 0.49 ± 0.01 0.53 ± 0.06 Cinnamate 0.40 ± 0.01 0.44 ± 0.04 ୟ୮୮ େ ୟ୮୮ ୟ୮୮

| Inhibitor   | (a) K app I (mM) ୍ ୍భ ୍ analysis of experimental data on the effect of substrate concentration at different inhibitor concen-   | (b) K app I (mM)   |
|-------------|------------------------------------------------------------------------------------------------------------------------------|--------------------|
| Benzoate    | 0.49 ± 0.01 trations.                                                                                                        | 0.53 ± 0.06        |
| Cinnamate   | 0.40 ± 0.01                                                                                                                  | 0.44 ± 0.04        |

(a)

K

(mM) obtained from

𝑖

ୈ

, (

IC

= (1 + n)K

) with n = 1; (b)

K

(mM) obtained from the

(a) K app I (mM) obtained from i D, (IC C 50 = ( 1 + n ) K app I 1 ) with n = 1; (b) K app I (mM) obtained from the analysis of experimental data on the effect of substrate concentration at different inhibitor concentrations. The chemical structures of these compounds and their derived analogous are shown in Figure 2.

<!-- image -->

## Benzoate

<!-- image -->

Cinnamate

(2-(3-methoxyphenoxy)-2-oxoethyl (E)-3-(4-hydroxyphenyl) acrylate)

).

(2-(3-methoxyphenoxy)-2-oxoethyl 2,4-dihydroxybenzoate)

<!-- image -->

Molecules

2022

,

27

, x FOR PEER REVIEW

6 of 22

The dockings of benzoate and cinnamate to oxy-tyrosinase and met-tyrosinase are

shown in Figures 3 and 4.

<!-- image -->

Molecules

2022

,

27

Figure 3. Docking of benzoate ( A , B ) and cinnamate ( C , D ) to oxy -tyrosinase. The binuclear active copper site in thin sticks ( A , C ) and the whole structure of oxy -tyrosinase in ribbons ( B , D ) are depicted with the ligands. The atom colours are as follows: oxygen = red, nitrogen = blue, copper = brown, white = hydrogen, and carbon = green. Ligands are shown in thick sticks and tyrosinase residues in thin sticks. Figure 3. Docking of benzoate ( A , B ) and cinnamate ( C , D ) to oxy -tyrosinase. The binuclear active copper site in thin sticks ( A , C ) and the whole structure of oxy -tyrosinase in ribbons ( B , D ) are depicted with the ligands. The atom colours are as follows: oxygen = red, nitrogen = blue, copper = brown, white = hydrogen, and carbon = green. Ligands are shown in thick sticks and tyrosinase residues in thin sticks. , x FOR PEER REVIEW 7 of 22Figure 4. Cont .

<!-- image -->

Figure 4. Docking of benzoate ( A , B ) and cinnamate ( C , D ) to met -tyrosinase. The binuclear active copper site in thin sticks ( A , C ) and the full structure of met -tyrosinase in ribbons ( B , D ) are depicted with the ligands. Colour scheme is as in Figure 3. Figure 4. Docking of benzoate ( A , B ) and cinnamate ( C , D ) to met -tyrosinase. The binuclear active copper site in thin sticks ( A , C ) and the full structure of met -tyrosinase in ribbons ( B , D ) are depicted with the ligands. Colour scheme is as in Figure 3.

<!-- image -->

Table 2.

Compounds described as true inhibitors: competitive, non-competitive, uncompetitive and

mixed. Kd is the ligand dissociation constant of docking to the active site of oxy- and met-tyrosinase. Oxy Met Table 2. Compounds described as true inhibitors: competitive, non-competitive, uncompetitive and mixed. K d is the ligand dissociation constant of docking to the active site of oxy- and met-tyrosinase.

| Figures                                            | Compound Name                                                                                     | Kd (mM)  Competitive  2.76 Inhibition Type   | Kd (mM)  Oxy       | Met      | References   |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------|--------------------|----------|--------------|
| Figures 3A,B and 4A,B                              | Benzoate                                                                                          | Kd (mM)  Competitive  2.76 Inhibition Type   | 0.072 K d (mM)     | K d (mM) | [13]         |
| Figures 3C,D and 4C,D  Figure 3A,B and Figure 4A,B | Cinnamate  Benzoate                                                                               | Competitive  3.73 Competitive                | 0.016 2.76         | 0.072    | [13]  [13]   |
| Figure S8  2 ' Figure 3C,D and Figure 4C,D         | ' -biphenyl]-2,4-diol  Cinnamate                                                                  | Competitive  14.05 Competitive               | 1.86  3.73         | 0.016    | [26]  [13]   |
| Figure S9  Figure S8                               | -(Hydroxymethyl)-[1,1 trans-3,4-Diflurocinnamate  2 ' -(Hydroxymethyl)-[1,1 ' -biphenyl]-2,4-diol | Competitive  3.29  Competitive               | 0.14  14.05        | 1.86     | [27]  [26]   |
| Figure S9                                          | trans-3,4-Diflurocinnamate                                                                        | Competitive                                  | 3.29               | 0.14     | [27]         |
| Figure S10  Figure S10                             | 6-Fluoro-1H-indazole  6-Fluoro-1H-indazole                                                        | Non-competitive  0.5  Non-competitive        | 0.77  0.5          | 0.77     | [28]  [28]   |
| Figure S10  Figure S10                             | 7-Fluoro-1H-indazole  7-Fluoro-1H-indazole                                                        | Non-competitive  0.5  Non-competitive        | 0.6  0.5           | 0.6      | [28]  [28]   |
| Figure S10  Figure S10                             | 4-Chloro-1H-indazole  4-Chloro-1H-indazole                                                        | Non-competitive  0.5  Non-competitive        | 0.4  0.5           | 0.4      | [28]  [28]   |
| Figure S10  Figure S10                             | 6-Bromo-1H-indazole  6-Bromo-1H-indazole                                                          | Non-competitive  0.47  Non-competitive       | 0.9  0.47          | 0.9      | [28]  [28]   |
| Figure S10                                         | 7-Bromo-1H-indazole                                                                               | Non-competitive                              | 0.47               | 0.34     | [28]         |
| Figure S10  Figure S11                             | 7-Bromo-1H-indazole  2-Aminobenzoate                                                              | Non-competitive  0.47  Non-competitive       | 0.34  1.87         | 0.052    | [28]  [29]   |
| Figure S11  Figure S11                             | 2-Aminobenzoate  4-Aminobenzoate                                                                  | Non-competitive  1.87  Non-competitive       | 0.052  2.17        | 0.081    | [29]  [29]   |
| Figure S11  Figure S15                             | 4-Aminobenzoate  Propyl gallate                                                                   | Non-competitive  2.17  Mixed                 | 0.081  3.91        | 0.68     | [29]  [30]   |
| Figure S15  Figure S17                             | Propyl gallate  Sanggenone C                                                                      | Mixed  3.91  Competitive                     | 0.68  255.29       | 0.034    | [30]  [31]   |
| Figure S17  Figure S25                             | Sanggenone C  (E)-2-Acetyl-5-methoxyphenyl-3-(4- methoxyphenyl)acrylate                           | Competitive  Mixed                           | 255.29  0.034  0.3 | 0.46     | [31]  [32]   |

Figures

Compound Name

Inhibition Type

References

Figure S25

(E)-2-Acetyl-5-methoxyphenyl-3-(4-

methoxyphenyl)acrylate

Mixed

0.3

0.46

[32]

The chemical structures of these compounds and their derived analogous are shown in Figure 2.

The dockings of benzoate and cinnamate to oxy-tyrosinase and met-tyrosinase are shown in Figures 3 and 4.

2.3. Discussion about the Relationship of IC 50 and the Values of the Inhibition Constant K app I with Data from the Literature for Tyrosinase

While conducting a literature review of recently published tyrosinase inhibition studies, we sometimes observed that there was a lack of correlation between the IC 50 values and the K app I values. Next, some cases are described for the different types of inhibition.

## 2.3.1. With Reference to Competitive Inhibitors

The study of tyrosinase inhibition can be carried out on diphenolase, monophenolase activity or both. When the study is carried out using L-tyrosine as a substrate (monophenolase activity), the existence of a transition phase must be taken into account, which causes a delay period, t , before the system reaches a steady state [12]. In a previous work, our group showed the usefulness of adding, at t = 0, the necessary amount of L-dopa to reach the steady state and to be able to obtain correct measurements of the initial velocity [13].

pounds are shown in Figure S1.

petitive  inhibitors;  the  inhibition

16.55 μM IC

K

ୟ୮୮

୍

ହ଴

= 3.70 ± 0.51 μM

= 3.01 μM IC

(a) and (b) that

= 5.00 ± 0.

, whic

K

ହ଴

ୟ୮୮

୍

the chemical structure of

cules could behave as alternative

Benzimidazothiazolone derivatives are tyrosinase inhibitors [33]. An inhibition study was carried out using L-tyrosine as substrate and the values obtained for the compounds are shown in Figure S1. It was established that the three compounds a-c are competitive inhibitors; the inhibition constants and the IC 50 described are: (a) K app I = 16.55 µ M IC 50 = 3.70 ± 0.51 µ M; (b) K app I = 3.21 µ MIC 50 = 3.05 ± 0.95 µ Mand (c) K app I = 3.01 µ M IC 50 = 5.00 ± 0.38 µ M. From these values it becomes clear for compounds (a) and (b) that K app I > IC 50 , which is not in agreement with Equation (S20). In addition, the chemical structure of the compounds described in Figure S1 shows that these molecules could behave as alternative substrates to L-tyrosine, and this would also lead to a distortion in the initial velocity measurements and therefore of K app I and IC 50 . In the presence of L-dopa accumulated in the medium when the enzyme acts on L-tyrosine, these compounds can behave as alternative substrates to L-tyrosine. Regarding the docking, the compounds bind with practically the same affinity to the met and oxy forms (Table 3). The docking is shown in Figures S2-S4. In addition, it should be noted that the distance of the oxygen from the peroxide group in the oxy-tyrosinase form is less than 2.9 distortion in the initial velocity meas ence of L-dopa accumulate compounds can behave as alternativ compounds bind with practicall docking is shown in Figures S2-S oxygen from the peroxide group in position of the phenolic hy reaction can occur and behave as kinetic deviations. On the ot can be a substrate for the enzyme, met-tyrosinase (Table 3). Note that period, and if it is not eliminated, it [13]. Ᾰ Scheme S2 shows how a mo dopa. The met-tyrosinase form is ina is capable of hydroxylating it if cert tyrosinase form acting on Lfor the ortho position of the phenolic hydroxyl of the compound, in such a way that the hydroxylation reaction can occur and behave as an alternative substrate; this could be the origin of the kinetic deviations. On the other hand, compound b, due to its ortho-diphenolic structure, can be a substrate for the enzyme, as shown in Figure S3A,B in the docking to oxy and mettyrosinase (Table 3). Note that when using L-tyrosine as a substrate there is a delay period, and if it is not eliminated, it can lead to erroneous initial velocity measurements [13].

Scheme S2 shows how a monophenol can behave as an alternative substrate to L-dopa. The met-tyrosinase form is inactive on the monophenol, but the oxy-tyrosinase form is capable of hydroxylating it if certain requirements are met. On the other hand, the mettyrosinase form acting on L-dopa (measured substrate) enters the catalytic cycle.

In the study of urolithin and reduced urolithin derivatives as potent inhibitors of tyrosinase [26], the compounds described in Figure S5 show competitive inhibition with IC 50 values of (a) 18.09 ± 0.25 µ M, (b) 4.14 ± 0.10 and (c) 15.69 µ M. The values of K app I described are: 2 µ M, 0.4 µ Mand 3 µ M. In this case, it is true that IC 50 > K app I , but these values imply, according to Equation (S20), IC 50 = K app I ( 1 + n ) , which has been worked out at values of n = [ D ] 0 /K D m of 8, 10 and 4. In addition, the chemical structure of the three compounds indicates that they could be substrates of the enzyme (Figure S5), and the docking data are shown in Tables 2 and 3. Figures S6-S8 show the docking to tyrosinase of these compounds. The compounds a (Figure S6) and b (Figure S7) from Figure S5 could be alternative substrates (Table 3). Compound c (Figure S8) from Figure S5 is shown as a true competitive inhibitor (Table 2).

The study of cinnamate derivatives on tyrosinase monophenolase and diphenolase activities suggests that trans-3,4-difluorocinnamic acid (Figure S9) behaves as a competitive inhibitor (Table 2), with a value of K app I = 197 ± 11 µ M and an IC 50 value of 0.78 ± 0.02 mM, which approximately satisfies the Equation (S20) IC 50 = K app I ( 1 + n ) . However, the degrees of inhibition for monophenolase ( i M ) and diphenolase ( i D ) activity for the compound trans-3,4 difluorocinnamic acid, since it is a competitive inhibitor, should be the same [13]. Furthermore, i M = 68.6 ± 4.2 µ Mand i D = 780 ± 2 µ M, and the problem stems from the fact that the inhibition study has been conducted through the measurement of monophenolase activity with L-tyrosine, so the lag is not eliminated and the speeds obtained may not be correct [27]. This compound essentially binds to the met form, according to the docking data (Table 2).

;

compounds bind with practically the same affinity to the met an

docking is shown in Figures S2-S4. In addition, it should be not

oxygen from the peroxide group in the oxy-tyrosinase form is le

position of the phenolic hydroxyl of the compound, in such a w

reaction can occur and behave as an alternative substrate; this

kinetic deviations. On the other hand, compound b, due to its

Table 3. Compounds described as inhibitors: competitive, non-competitive, uncompetitive and mixed, which can behave as alternative substrates or as suicide substrates. K d is the ligand dissociation constant of docking to the active site of oxy and met -tyrosinase. d-O 2 corresponds to the distance from the oxygen atoms of the peroxide group of oxy -tyrosinase to a carbon atom adjacent to a -OH group. can be a substrate for the enzyme, as shown in Figure S3A, met-tyrosinase (Table 3). Note that when using L-tyrosine as period, and if it is not eliminated, it can lead to erroneous init [13].

| Figures             |                                                                           | Inhibition Type               | Oxy      | Oxy        | Met      | Possible Alternative                                                   | References   |
|---------------------|---------------------------------------------------------------------------|-------------------------------|----------|------------|----------|------------------------------------------------------------------------|--------------|
|                     | Compound Name                                                             | Proposed                      | K d (mM) | d-O2 ( Ᾰ ) | K d (mM) | Substrate                                                              |              |
| Figure 5A,B         | [2-(3-Methoxyphenoxy)-2-oxoethyl] 2,4-dihydroxybenzoate                   | Non-competitive               | 0.5      | 2.8        | 0.25     | Monophenol                                                             | [34]         |
| Figure 6A,B         | 2-(3-methoxyphenoxy)-2-oxoethyl-(E)-3-(4-hydroxyphenyl) acrylate          | Non-competitive               | 0.36     | 2.8        | 0.25     | Scheme S2 shows how a monophenol can behave as an  Monophenol          | [34]         |
| Figure S2           | (Z)-2-(4-Hydroxybenzylidene)benzo[4,5]imidazo[2,1-b]thiazol-3(2H)-one     | Competitive                   | 0.14     | 2.9        | 0.15     | dopa. The met-tyrosinase form is inactive on the monophenol Monophenol | [33]         |
| Figure S3A,B        | (Z)-2-(3,4-Dihydroxybenzylidene)benzo[4,5]imidazo[2,1-b]thiazol-3(2H)-one | Competitive                   | 0.14     | -          | 0.089    | is capable of hydroxylating it if certain requirements ar o -Diphenol  | [33]         |
| Figure S4           | (Z)-2-(2,4-Dihydroxybenzylidene)benzo[4,5]imidazo[2,1-b]thiazol-3(2H)-one | Competitive                   | 0.25     | 2.7        | 0.19     | Monophenol                                                             | [33]         |
| Figure S6           | 1,3-Dihydroxy-6H-benzo[c]chromen-6-one                                    | Competitive                   | 0.71     | 3.7        | 0.34     | tyrosinase form acting on L-dopa (measured substrate) Monophenol       | [26]         |
| Figure S7           | 1,3-Dihydroxy-8-methoxy-6H-benzo[c]chromen-6-one                          | Competitive                   | 0.99     | 3.7        | 0.51     | Monophenol                                                             | [26]         |
| Figures S13 and S14 | Luteolin                                                                  | Uncompetitive Non-competitive | 1.1      | -          | 14.57    | o -Diphenol                                                            | [35]         |
| Figure S18          | Oxyresveratrol                                                            | Non-competitive               | 4.8      | 4.8        | 1.18     | Monophenol                                                             | [31]         |
| Figure S19A,B       | L-Epicatechin                                                             | Competitive                   | 3.84     | -          | 4.9      | o -Diphenol                                                            | [31]         |
| Figure S20A,B       | Catechin                                                                  | Competitive                   | 3.87     | -          | 2.27     | o -Diphenol                                                            | [31]         |
| Figure S22A,B       | N-trans-Caffeoyltyramine                                                  | Competitive                   | 1.5      | -          | 0.15     | o -Diphenol                                                            | [36]         |
| Figure S23          | N-trans-feruloyltyramine                                                  | Competitive                   | 0.093    | 2.9        | 0.038    | Monophenol                                                             | [36]         |
| Figure S24          | N-trans-Coumaroyltyramine                                                 | Competitive                   | 0.067    | 2.8        | 0.032    | Monophenol                                                             | [36]         |
| Figure S26          | (E)-2-Acetyl-5-methoxyphenyl-3-(4-hydroxyphenyl)acrylate                  | Non-competitive               | 0.11     | 2.8        | 0.115    | Monophenol                                                             | [32]         |
| Figure S27          | (E)-2-Isopropyl-5-methylphenyl-3-(4-hydroxyphenyl)acrylate                | Mixed                         | 0.15     | 2.8        | 0.12     | Monophenol                                                             | [32]         |
| Figure S29          | Streblus C                                                                | Competitive                   | 0.076    | 2.7        | 0.071    | Monophenol                                                             | [37]         |
| Figure S30          | Streblus D                                                                | Competitive                   | 1.3      | 3.4        | 0.24     | Monophenol                                                             | [37]         |

## 2.3.2. With Reference to Non-Competitive Inhibitors

Non-competitive inhibition of tyrosinase by indazoles has been described (Figure S10) [28]. The values described for K app I are always greater than the IC 50 , and a possible explanation for this could be that the activity measurements are made with catechol, which derives a very unstable o -quinone after its oxidation. These compounds, according to docking studies, bind practically with the same affinity to the met and oxy forms (Table 2).

On the other hand, the study of tyrosinase inhibition by 2-aminobenzoic acid and 4-aminobenzoic acid shows strict compliance with Equation (S22), and non-competitive inhibition [29] (Chemical structures are shown in Figure S11), obtaining IC 50 values = 4.72 µ M and 20 µ Mwith values of K app I = 4.72 µ Mand 20 µ M, respectively. The affinity of these compounds for the met form is much higher than for the oxy form, according to the docking data (Table 2). The presence of peroxide in the oxy-tyrosinase form makes the union of these compounds weaker (Table 2).

Inhibition of tyrosinase by hydroxyl-substituted benzoate/cinnamate derivatives has recently been reported (Figure 2) [34]. In this work, the IC 50 values described do not correlate quantitatively with the K app I values described by Equation (S20). Benzoate and cinnamate are competitive inhibitors, so these derivatives are expected to behave in the same way, but this is not the case, and they are described as non-competitive. A possible explanation for this could be that the same substrate concentration range is used for different inhibitor concentrations. In addition, these molecules have a free hydroxyl, which could be an enzyme substrate (Table 3 (see later)) which would distort the kinetic analysis (see Figure 2).

## 2.3.3. With Reference to Uncompetitive Inhibitors

Inhibition of tyrosinase by a component of Moringa oleifera extract (Figure S12) has been described [35]. The type of inhibition described is uncompetitive, with an IC 50 =121.3 ± 0.4 µ g/mL and K app I = 73 µ g/mL. As luteolin is the main component of the extract, these data would be in agreement with a study published a few years ago [38] where an inhibition constant value of 103 µ Mand an uncompetitive type of inhibition were proposed. However, luteolin has recently been described as a non-competitive inhibitor with K app I = 291.75 ± 7.75 µ M[39]. These discrepancies of reversible uncompetitive and non-competitive inhibition can be explained by the chemical structure of luteolin (Figure S12), which, like any compound with a diphenolic structure, behaves as a substrate of tyrosinase [39]. The affinity of luteolin for met-tyrosinase is low (Table 3). Docking of luteolin to oxy-tyrosinse is shown in Figure S13 and docking to met-tyrosinase in Figure S14. Because this molecule carries an o -diphenolic structure, it is oxidized by both met-tyrosinase and oxy-tyrosinase (Table 3).

## 2.3.4. With Reference to Mixed-Type Inhibitors

The inhibition of tyrosinase by propylgallate is of the mixed type (Figure S15), with an IC 50 value of 0.685 mM and with values of K app I 1 = 0.661 mM and K app I 2 = 2.135 mM. According to data from the docking (Table 2), this compound binds better to the met form than to the oxy [30]. The IC 50 value that is obtained by applying the formula described in the supplementary material Equation (S35) is 1 mM, and the value described experimentally is 0.685 mM.

## 2.4. Other Possible Causes of the Lack of Correlation between IC 50 and K app I

## 2.4.1. Inhibitor Can Be Alternative Substrate

Benzoate and cinnamate are competitive inhibitors of tyrosinase diphenolase activity [13]. In this sense, for the derivatives of benzoate and cinnamate studied in [34], a competitive type of behaviour should be expected, but what is described is a 'non-competitive' behaviour. It is noteworthy that the quantitative relationship Equation (S19) between the values of IC 50 and K app I is not fulfilled. Thus, (2-(3-methoxyphenoxy)-2-oxoethyl-2,4dihydroxybenzoate) (compound a) had an IC 50 value of 23.8 µ M, while the K app I value was 130 µ M. On the other hand, (2-(3-methoxyphenoxy)-2-oxoethyl-(E)-3-(4-hydroxyphenyl)

Molecules

2022

,

27

Molecules

2022

,

27

the chemical structure of the compounds described in Figure

cules could behave as alternative substrates to L-tyrosine, an

distortion in the initial velocity measurements and therefore of

ence of L-dopa accumulated in the medium when th

11 of 22 compounds can behave as alternative substrates to L-tyrosine.

compounds bind with practically the same affinity to the met a

docking is shown in Figures S2-S4. In addition, it should be

acrylate) (compound b) inhibited tyrosinase with an IC 50 value of 5.7 µ M, while the K app I value was 11 µ M. The structures of these compounds are shown in Figure 2, and it could be proposed that they may be substrates of the enzyme. This would result in obtaining incorrect initial rates. oxygen from the peroxide group in the oxy-tyrosinase form is l position of the phenolic hydroxyl of the compound, in such reaction can occur and behave as an alternative substrate; this kinetic deviations. On the other hand, compound b, due to its

The docking of benzoate and cinnamate to met-tyrosinase and oxy-tyrosinase is shown in Figures 3 and 4. The docking of benzoate derivatives Figure 2a is shown in Figure 5 and that of cinnamate derivatives Figure 2b in Figure 6. From the data shown in Table 3, these compounds have practically the same affinity towards oxy-tyrosinase and met-tyrosinase and the distance of the oxygen from the peroxide in the oxy form to the ortho position with respect to the phenolic hydroxyl is 2.8 can be a substrate for the enzyme, as shown in Figure S3A, met-tyrosinase (Table 3). Note that when using L-tyrosine as period, and if it is not eliminated, it can lead to erroneous init [13]. Ᾰ . This is adequate to produce the hydroxylation reaction, and this could be the origin of the change in the type of inhibition. , x FOR PEER REVIEW 12 of 22 , x FOR PEER REVIEW 12 of 22

Scheme S2 shows how a monophenol can behave as an

dopa. The met-tyrosinase form is inactive on the monophenol

is capable of hydroxylating it if certain requirements ar

tyrosinase form acting on L-dopa (measured substrate)

Figure 5. Docking of [2-(3-methoxyphenoxy)-2-oxoethyl] 2,4-dihydroxybenzoate to oxy-tyrosinase ( A ) and met-tyrosinase ( B ). Colour scheme is as in Figure 3. Figure 5. Docking of [2-(3-methoxyphenoxy)-2-oxoethyl] 2,4-dihydroxybenzoate to oxy-tyrosinase ( A ) and met-tyrosinase ( B ). Colour scheme is as in Figure 3. Figure 5. Docking of [2-(3-methoxyphenoxy)-2-oxoethyl] 2,4-dihydroxybenzoate to oxy-tyrosinase ( A ) and met-tyrosinase ( B ). Colour scheme is as in Figure 3.

<!-- image -->

Figure 6. Docking of (2-(3-methoxyphenoxy)-2-oxoethyl-(E)-3-(4-hydroxyphenyl) acrylate) to oxytyrosinase ( A ) and met-tyrosinase ( B ). Colour scheme is as in Figure 3. Figure 6. Docking of (2-(3-methoxyphenoxy)-2-oxoethyl-(E)-3-(4-hydroxyphenyl) acrylate) to oxytyrosinase ( A ) and met-tyrosinase ( B ). Colour scheme is as in Figure 3. Figure 6. Docking of (2-(3-methoxyphenoxy)-2-oxoethyl-(E)-3-(4-hydroxyphenyl) acrylate) to oxytyrosinase ( A ) and met-tyrosinase ( B ). Colour scheme is as in Figure 3.

<!-- image -->

From the chemical structure of the two compounds shown in Figure 2a,b, a hydroxyl

From the chemical structure of the two compounds shown in Figure 2a,b, a hydroxyl

group can be seen in position 4. Docking studies in Figures 5 and 6 show that the two

group can be seen in position 4. Docking studies in Figures 5 and 6 show that the two

compounds bind with high affinity for the hydroxyl in position 4, and also the distance of

compounds bind with high affinity for the hydroxyl in position 4, and also the distance of

From the chemical structure of the two compounds shown in Figure 2a,b, a hydroxyl group can be seen in position 4. Docking studies in Figures 5 and 6 show that the two compounds bind with high affinity for the hydroxyl in position 4, and also the distance of the oxygens of oxy-tyrosinase to the ortho position is adequate for the electrophilic aromatic substitution reaction to occur (Table 3) [40-42]. In this way, these compounds would possibly behave as alternative substrates to L-dopa. In the case of 4-hydroxycinnamic and 3-hydroxycinnamic, it was shown that they were alternative substrates to L-tyrosine and L-dopa [43,44]. The interactions with the hydroxyl group at positions 3 and 4 and the distances of the oxygens in oxy-tyrosinase to the ortho positions make hydroxylation possible [43,44].

## 2.4.2. Inhibitor Can Be a Suicide Substrate

In general, o -diphenols are suicide substrates of tyrosinase with different inactivation potency. In Scheme S2, the action of a possible inhibitor with an o -diphenolic group is shown, and this compound could be oxidized by both met-tyrosinase and oxy-tyrosinase. Furthermore, it should be noted that o -diphenols are suicide substrates of the enzyme. The same substrate used to measure L-dopa activity is also a suicide substrate, but the important thing is the time that the enzyme and o -diphenol are in contact. The suicidal action of L-dopa is minimal because the measurements are made at short times, but as in many inhibition assays, the enzyme is preincubated with the inhibitor ( o -diphenol) from 10 to 30 min; the effect of suicide inactivation is relevant and this can lead to distortion of the kinetic analysis.

Figure S3A,B shows the docking of compound (Z)-2-(3,4-Dihydroxybenzylidene) benzo[4,5]imidazo[2,1-b]thiazol-3(2H)-one to oxy-tyrosinase and met-tyrosinase. This compound can behave as a suicide substrate and cause deviations in the determination of kinetic parameters.

Figures S13 and S14 show the docking of luteolin to oxy- and met-tyrosinase. Due to the o -diphenolic structure, this compound can be a substrate of the enzyme and have suicide behaviour [39].

In the case of propyl gallate (Figure S15), the IC 50 value is 0.685 mM, lower than the theoretical value obtained from K app I 1 and K app I 2 . This slight increase in the strength of the inhibitor may be because these trihydroxylated compounds are suicide substrates of tyrosinase, as was shown long ago [45,46].

Tyrosinase inhibition by four polyphenols from Morus and tulles Barley has been studied [31]. These compounds have been described as competitive inhibitors (Figure S16): sanggenone C (IC 50 =18.85 µ M); L-epicatechin (IC 50 =191.99 µ M); catechin (IC 50 = 511.59 µ M). Non-competitive inhibition has been reported for oxyresveratrol (IC 50 = 4.50 µ M). The K app I values described were: sanggenone C 11.92 µ M; L-epicatechin 119.16 µ M; catechin 365.86 µ M and oxyresveratrol 4.50 µ M. The assay methodology is similar to the cases described above with preincubations of the enzyme and the inhibitor dissolved in DMSO for 10 min. The reaction is started by adding L-dopa at a concentration equal to K D m , and the IC 50 values should meet the relationship IC 50 = K app I ( 1 + n ) . With n = 1, these would be IC 50 = 2K app I ; however, the IC 50 values do not satisfy Equation (S20). In the case of oxyresveratrol, it is true that IC 50 ∼ = K app I , because it is a non-competitive type of inhibitor and could also be a substrate for the enzyme in the presence of H 2 O 2 or L-dopa [47,48]. The docking results are shown in Table 3. In the case of sanggenone C, the compound acts as a competitive inhibitor (Table 2), acting on met-tyrosinase (Figure S17). The chemical structure of catechin and epicatechin show an o -diphenol, and they are substrates of the enzyme, as demonstrated experimentally [49]. The low IC 50 values would be justified because these compounds are suicide substrates (Scheme S2) of the enzyme and a 10 min preincubation is performed in the assay [49]. The values of the dissociation constants obtained from the docking are shown in Table 3. The docking Figures are described in Figures S18, S19A,B and S20A,B.

(a) and (b) that

K

୍

> IC

ହ଴

, which is not in agreement wi

(a) and (b) that

K

୍

> IC

ହ଴

, which is not in

the chemical structure of the compounds described

the chemical structure of the compounds descri

cules could behave as alternative substrates to L-tyrosine, an

cules could behave as alternative substrates to L-

distortion in the initial velocity measurements and theref

distortion in the initial velocity measurements an

13 of 22 ence of L-dopa accumulated in the medium when th ence of L-dopa accumulated in the medium

compounds can behave as alternative substrates to L-tyrosi

compounds can behave as alternative substrates

compounds bind with practically the same affinity to the met a

compounds bind with practically the same affini

When the anti-melanogenesis and anti-tyrosinase power of phenethyl cinnamamides compounds from an extract of hemp ( Cannabis sativa L.) was studied, it was found that among the compounds studied (Figure S21) [36], the most potent is the N-trans-caffeoyltyramine. Its diphenolic structure can cause the suicide inactivation of the enzyme, since in the inhibition test it is preincubated with tyrosinase for 30 min and then the reaction is started with L-dopa, in addition to an additional 10 min incubation. The three inhibitors, according to the docking data (Table 3), can be substrates of the enzyme, joining through the phenolic hydroxyl group corresponding to tyramine, in addition to compound (a), which due to its diphenolic structure, can be a suicide substrate. The dockings are shown in Figures S22A,B, S23 and S24. The distance of the oxygen from the peroxide to the ortho position of the phenolic hydroxyl is 2.8 docking is shown in Figures S2-S4. In addition, it should be oxygen from the peroxide group in the oxy-tyrosinase form is position of the phenolic hydroxyl of the compound, in such reaction can occur and behave as an alternative substrate; thi kinetic deviations. On the other hand, compound b, due to its can be a substrate for the enzyme, as shown in Figure S3A, met-tyrosinase (Table 3). Note that when using L-tyrosine as period, and if it is not eliminated, it can lead to erroneous in [13]. Ᾰ and 2.9 docking is shown in Figures S2-S4. In addition, it oxygen from the peroxide group in the oxy-tyrosi position of the phenolic hydroxyl of the comp reaction can occur and behave as an alternative su kinetic deviations. On the other hand, compound can be a substrate for the enzyme, as shown in met-tyrosinase (Table 3). Note that when using Lperiod, and if it is not eliminated, it can lead to er [13]. Ᾰ , respectively, and therefore they can act as alternative substrates.

Scheme S2 shows how a monophenol can behave as an

Scheme S2 shows how a monophenol can be

dopa. The met-tyrosinase form is inactive on the monophenol

dopa. The met-tyrosinase form is inactive

## 2.4.3. Enzyme Inhibition Assay Design

is capable of hydroxylating it if certain requirements ar tyrosinase form acting on L-dopa (measured substrate) is capable of hydroxylating it if certain requir tyrosinase form acting on L-dopa (measure In performing tyrosinase inhibition assays, several aspects must be considered in order to avoid false interpretations, as described below:

## Preincubations and Use of Organic Solvents

It is common in tyrosinase inhibition assays to preincubate the enzyme with the inhibitor for a long time, and to subsequently start the reaction with the substrate. This procedure can give erroneous values of the inhibited rate (V 0,i ) due to a possible reaction of the inhibitor with the enzyme [32]. Kinetic studies have been carried out on the inhibition and inactivation of tyrosinase by DMSO in the presence of substrate, and the inhibition constant of the free enzyme and of the enzyme-substrate complex has been determined. From these studies, it is shown that at low concentrations of DMSO, the inhibition is reversible, and at high concentrations, the enzyme is irreversibly inactivated. In addition, these works indicate that the substrate protects the enzyme from inactivation [50-52]. Inhibition of tyrosinase by cinnamate esters has been studied [32], showing that they are more potent than their parent compounds, see Figure S25a-c [32]. The calculated values for the IC 50 parameter are: 2.0 µ M; 8.3 µ Mand 10.6 µ Mand the values of K app I and the type of inhibition were: (a) non-competitive and K app I = 3.8 µ M; (b) mixed K app I = 10.0 µ M and K app IS = 35.6 µ M(c) mixed and K app I = 8.0 µ Mand K app IS = 72.2 µ M. Theoretical IC 50 values calculated from Equation (S35) are 15.6 µ Mand 7.20 µ M. Note that the IC 50 value for cinnamate is 209.5 µ M, lower than that described in [13]. An explanation for this could be the inactivating effect of DMSO and the long incubation time. It is noteworthy that 4-hydroxycinnamic has a value of 4708.5 µ M[32] as it is a substrate, which is in agreement with that described in [43]. Compounds (a) and (b) could behave as alternative substrates (Table 3); however, compound (c) is a true inhibitor (see Table 2). The dockings of (a) and (b) to Eox are shown in Figures S26 and S27.

Tyrosinase inhibition by two new stilbenes extracted from stems of Streblus Ilicifolius has been described. (Figure S28) [37]. Compound (a) bears a resorcinol end and is much more inhibitory than (b) which bears a phenol. On the other hand, the inhibition assay again involves the inhibitor dissolved in DMSO and a 30 min preincubation with which the DMSO can inactivate the enzyme. The reaction is subsequently started by adding L-dopa and is incubated again for 7 min. In our opinion, the design of the inhibition test is not adequate, and also, in the presence of L-dopa, these compounds could be alternative substrates. Compound (a) binds oxy better than (b) (Table 3). Figures of the docking of tyrosinase to these two compounds are shown in Figures S29 and S30. These compounds, especially streblus C, can behave as alternative substrates (Table 3).

## 2.5. Proposal for an Experimental Design to Determine the Type and Strength of a Tyrosinase Inhibitor from i D Values

An experimental design is proposed together with data analysis that allows several aspects to be determined with a few experiments-the IC 50 value, the type of inhibition and

Molecules

2022

,

27

, x FOR PEER REVIEW

the K app I value. This design is described and carried out with data obtained by simulating the different mechanisms under study. This would be carried out in the following stages:

Step 1. Progress curves in the absence and presence of inhibitor, obtained by simulation, according to the differential equations corresponding to each mechanism of inhibition, described in the supplementary material. Determination of the i D values, varying the concentration of inhibitor, at a fixed substrate concentration [ D ] 0 = K D m (Table S1). Table S1 shows the data for the different types of inhibition considered in this paper. 15  of  23 Step 2. Representation of inhibition degree values versus inhibitor concentration. Fig-

Step 2. Representation of inhibition degree values versus inhibitor concentration. Figure 7 shows the values of i D vs. [ I ] 0 for each type of inhibition. ure 7 shows the values of 𝑖 D vs. [I] 0 for each type of inhibition.

Figure 7. ( A ) and (B ). Representation of the degrees of inhibition 𝑖 D obtained for each type of reversible and fast inhibition giving a hyperbolic behavior, against the inhibitor concentration. ( A ) a, competitive; b, uncompetitive; c, non-competitive. ( B ) d, mixed type (1) and e, mixed type (2). Conditions:  a.  Competitive: [E] 0 = 10 × 10 -9 M , [E ox ] 0 = 0.3 × [E] 0 , [E m ] 0 = 0.7 × [E] 0 ; [D] 0 = 0.5 × 10 -3 M ; [O 2 ] 0 = 0.26 × 10 -3 M , and the inhibitor concentration was varied according to (μM): 0, 10, 15, 30, 45, 60, 72.5, 100, 200 and 300. The rate constants were: k 2 = 5 × 10 6 M -1 s -1 , k -2 = 10 s -1 , k 3 = 900 s -1 , k 6 = 2.16 × 10 5 M -1 s -1 , k -6 = 10 s -1 , k 7 = 108 s -1 , k 8 = 2.3 × 10 7 M -1 s -1 , k -8 = 1.03 × 10 3 s -1 , k 11 = 10 6 M -1 s -1 , k -11 = 10 s -1 , k 14 = 10 5 M -1 s -1 , k -14 = 2.68 s -1 , k 16 = 10 s -1 . b. Uncompetitive. The simulation conditions were the same as in the previous case, but the new  inhibition  constants  were: k 12 = 10 6 M -1 s -1 , k -12 = 10 s -1 , k 14 = 10 5 M -1 s -1 , k -14 = 2.68 s -1 , k 15 = 10 5 M -1 s -1 , k -15 = 3 s -1 . c. Non-competitive. The simulation conditions were the same as in the first case, but the inhibition constants were: k 12 = 10 6 M -1 s -1 , k -12 = 10 s -1 , k 15 = 10 5 M -1 s -1 , k -15 = 3 s -1 . d. Mixed type (1). The simulation conditions were the same as in the first case, but the inhibitor concentrations were (μM): 0, 10, 15, 30, 45, 60, 72.5, 100, 200, 300, 500 and 700. The  inhibition  constants  were: k 11 = 10 6 M -1 s -1 , k -11 = 10 s -1 , k 12 = 10 6 M -1 s -1 , k -12 = 10 s -1 , k 14 = 10 5 M -1 s -1 , k -14 = 2.68 s -1 , k 15 = 10 5 M -1 s -1 , k -15 = 30 s -1 .  e,  Mixed  type  (2). The simulation conditions were the same as in the previous case, but the inhibition constants were: k 11 = 10 5 M -1 s -1 , k -11 = 30 s -1 , k 12 = 10 6 M -1 s -1 , k -12 = 10 s -1 , k 14 = 10 5 M -1 s -1 , k -14 = 2.68 s -1 , k 15 = 10 6 M -1 s -1 , k -15 = 10 s -1 . Figure 7. ( A , B ). Representation of the degrees of inhibition i D obtained for each type of reversible and fast inhibition giving a hyperbolic behavior, against the inhibitor concentration. ( A ) a, competitive; b, uncompetitive; c, non-competitive. ( B ) d, mixed type (1) and e, mixed type (2). Conditions: a. Competitive: [ E ] 0 = 10 × 10 -9 M, [ Eox ] 0 = 0.3 × [ E ] 0 , [ Em ] 0 = 0.7 × [ E ] 0 ; [ D ] 0 = 0.5 × 10 -3 M; [ O 2 ] 0 = 0.26 × 10 -3 M, and the inhibitor concentration was varied according to ( µ M): 0, 10, 15, 30, 45, 60, 72.5, 100, 200 and 300. The rate constants were: k 2 = 5 × 10 6 M -1 s -1 , k -2 = 10 s -1 , k 3 = 900 s -1 , k 6 = 2.16 × 10 5 M -1 s -1 , k -6 = 10 s -1 , k 7 = 108 s -1 , k 8 = 2.3 × 10 7 M -1 s -1 , k -8 = 1.03 × 10 3 s -1 , k 11 = 10 6 M -1 s -1 , k -11 = 10 s -1 , k 14 = 10 5 M -1 s -1 , k -14 = 2.68 s -1 , k 16 = 10 s -1 . b. Uncompetitive. The simulation conditions were the same as in the previous case, but the new inhibition constants were: k 12 = 10 6 M -1 s -1 , k -12 = 10 s -1 , k 14 = 10 5 M -1 s -1 , k -14 = 2.68 s -1 , k 15 = 10 5 M -1 s -1 , k -15 = 3 s -1 . c. Non-competitive. The simulation conditions were the same as in the first case, but the inhibition constants were: k 12 = 10 6 M -1 s -1 , k -12 = 10 s -1 , k 15 = 10 5 M -1 s -1 , k -15 = 3 s -1 . d. Mixed type (1). The simulation conditions were the same as in the first case, but the inhibitor concentrations were ( µ M): 0, 10, 15, 30, 45, 60, 72.5, 100, 200, 300, 500 and 700. The inhibition constants were: k 11 = 10 6 M -1 s -1 , k -11 = 10 s -1 , k 12 = 10 6 M -1 s -1 , k -12 = 10 s -1 , k 14 = 10 5 M -1 s -1 , k -14 = 2.68 s -1 , k 15 = 10 5 M -1 s -1 , k -15 = 30 s -1 . e, Mixed type (2). The simulation conditions were the same as in the previous case, but the inhibition constants were: k 11 = 10 5 M -1 s -1 , k -11 = 30 s -1 , k 12 = 10 6 M -1 s -1 , k -12 = 10 s -1 , k 14 = 10 5 M -1 s -1 , k -14 = 2.68 s -1 , k 15 = 10 6 M -1 s -1 , k -15 = 10 s -1 .

<!-- image -->

Step 3. Data analysis of 𝑖 D vs. [I] 0 by nonlinear regression according to Equation (S16). IC 50 is  determined for each inhibitor: competitive ( IC 50 C );  non-competitive ( IC 50 NC ); uncompetitive ( IC 50 U ); mixed type (1) ( IC 50 M 1 ) and mixed type (2) ( IC 50 M 2 ) (Table 4). Step 3. Data analysis of i D vs. [ I ] 0 by nonlinear regression according to Equation (S16). IC 50 is determined for each inhibitor: competitive (IC C 50 ); non-competitive (IC NC 50 ); uncompetitive (IC U 50 ); mixed type (1) (IC M 1 50 ) and mixed type (2) (IC M 2 50 ) (Table 4).

Table 4.

Determination of the

IC

Type

𝐈𝐂

Competitive

IC

Non-competitive

IC

C

50

NC

50

U

50

values for the different types of inhibition.

𝟓𝟎

(μM)

= 60.8

= 26.9

Table 4. Determination of the IC 50 values for the different types of inhibition.

| Type            | IC 50 ( µ M)    |
|-----------------|-----------------|
| Competitive     | IC C 50 = 60.8  |
| Non-competitive | IC NC 50 = 26.9 |
| Uncompetitive   | IC U 50 = 53.2  |
| Mixed type (1)  | IC M1 50 = 40.4 |
| Mixed type (2)  | IC M2 50 = 15.9 |

D fixed (Table S2).

Step 4. Determination of i D for [ D ] 0 = 2K m and with [ I ] 0

Step 5. Possible types of inhibition:

- A. i 2 K D m D < i K D m D : could be competitive.
- B. i m D = i m D : is non-competitive and K I 50 .
- 2 K D K D

app = IC NC

- C. D D : could be uncompetitive.
- i 2 K D m > i K D m
- D. i m D < i m D : ambiguity between competitive and mixed type (1).
- 2 K D K D
- E. i 2 K D m D > i K D m D : ambiguity between competitive and mixed type (2).

In case B, there is no ambiguity between the types of inhibition. It would be a noncompetitive inhibitor with IC NC 50 = K app I , from the value of IC NC 50 (Table 4). The constancy of the value of i D when varying the concentration of the substrate, the type of inhibition (non-competitive) and the strength of the inhibitor are obtained for K app I (26.9 µ M), as per Equation (S22). In all other cases, there is ambiguity, which needs to be resolved.

Step 6. Solution of the ambiguity between competitive inhibition and mixed type (1). Two i D values are obtained by simulation with [ D ] 0 = 5K D m and [ D ] 0 = 10K D m . If the inhibition decreases significantly (for example: from 25.77% to 16.11%) ( i D → 0), then it would be a competitive inhibitor. If the inhibition decreases slightly (for example: from 51.02% to 48.37%), then it could be a mixed type (1) inhibition. In any case, the adjustment of the experimental data of i D vs. n according to Equations (S17) and (S31) helps to discern between competitive inhibition and the mixed type (1) (Figure 8A,B). The inhibition constant (K app I 1 ) is determined by nonlinear regression adjustment of ( i D vs. n) according to Equation (S17) (Figure 8A). The determined value of K app I 1 must comply with the value of IC C 50 according to Equation (S20). For K app I 1 (Table 4), in the case of competitive inhibition and in the case of mixed type (1) inhibition, the adjustment is performed by nonlinear regression of ( i D vs. n) according to Equation (S31), determining K app I 1 and K app I 2 (Figure 8B). These values must comply with Equation (S35) and are described in Table 4.

Step 7. Solution of the ambiguity between uncompetitive and mixed type (2) inhibition. Figure 9A,B shows the values of i D obtained for the variation in [ D ] 0 at fixed inhibitor concentration.

Molecules

2022

,

27

, x FOR PEER REVIEW

17 of 22

cern between competitive inhibition and the mixed type (1) (Figure 8A,B). The inhibition

K

constant (

ୟ୮୮

୍

భ

) is determined by nonlinear regression adjustment of (

to Equation (S17) (Figure 8A). The determined value of

of

IC

ହ଴

according to Equation (S20). For

K

ୟ୮୮

୍

భ

K

ୟ୮୮

୍

భ

𝑖

ୈ

vs. n) according

must comply with the value

(Table 4), in the case of competitive inhibi-

tion and in the case of mixed type (1) inhibition, the adjustment is performed by nonlinear

𝑖

regression of (

ୈ

vs. n) according to Equation (S31), determining

K

ୟ୮୮

୍

భ

and

K

ୟ୮୮

୍

మ

8B). These values must comply with Equation (S35) and are described in Table 4.

Figure 8. ( A ) Solution of the ambiguity between competitive and mixed type (1) inhibition. Representation of 𝑖 ୈ vs. n. The simulation conditions were the same as in Figure 6A,B, but the inhibitor concentration ሾIሿ ଴ was constant (100 µM). The substrate concentration (mM) was varied: 0.25, 0.35, 0.5, 1, 2, 3, 5 and 10. The adjustment by non-linear regression ( 𝑖 ୈ େ vs. n), according to Equation (S17), Figure 8. ( A ) Solution of the ambiguity between competitive and mixed type (1) inhibition. Representation of i D vs. n. The simulation conditions were the same as in Figure 6A,B, but the inhibitor concentration [ I ] 0 was constant (100 µ M). The substrate concentration (mM) was varied: 0.25, 0.35, 0.5, 1, 2, 3, 5 and 10. The adjustment by non-linear regression ( i C D vs. n), according to Equation (S17), allows us to obtain K app I1 (K app I1 = 32.6 µ M). Note that this value, according to Equation (S20), meets the value of IC C 50 (Table 4), which confirms the inhibition mechanism. ( B ) If it is a type (1) mixed inhibitor (K app I1 < K app I2 ), the simulated data would not fit Equation (S17) but would fit Equation (S31), as shown in ( B ). In the latter case, K app I1 (K app I1 = 26.2 µ M) and K app I2 (K app I2 = 74.5 µ M) are determined. Note the fulfillment of Equation (S35), and therefore, the value of IC M1 50 , (Table 4), which confirms the inhibition mechanism. allows us to obtain K ୍భ ୟ୮୮ ( K ୍భ ୟ୮୮ = 32.6 μM ). Note that this value, according to Equation (S20), meets the value of IC ହ଴ େ (Table 4), which confirms the inhibition mechanism. ( B ) If it is a type (1) mixed inhibitor ( K ୍భ ୟ୮୮ < K ୍మ ୟ୮୮ ), the simulated data would not fit Equation (S17) but would fit Equation (S31), as shown in ( B ). In the latter case, K ୍భ ୟ୮୮ ( K ୍భ ୟ୮୮ = 26.2 μM ) and K ୍మ ୟ୮୮ ( K ୍మ ୟ୮୮ = 74.5 μM ) are determined. Note the fulfillment of Equation (S35), and therefore, the value of IC ହ଴ ୑భ , (Table 4), which confirms the inhibition mechanism. Step 7. Solution of the ambiguity between uncompetitive and mixed type (2) inhibition. Figure 9A,B shows the values of 𝑖 ୈ obtained for the variation in ሾDሿ ଴ at fixed inhibitor concentration.

<!-- image -->

Figure 9. ( A ) and ( B ). Solution of the ambiguity between uncompetitive and mixed type (2) inhibition. Obtaining 𝑖 ୈ by varying ሾDሿ ଴ at fixed inhibitor concentration. ( A ) ( ሾIሿ ଴ = 30 µM). Representing 𝑖 ୈ vs. n, if a hyperbola is obtained that passes through the origin of coordinates, it could be an Figure 9. ( A , B ). Solution of the ambiguity between uncompetitive and mixed type (2) inhibition. Obtaining i D by varying [ D ] 0 at fixed inhibitor concentration. ( A ) ( [ I ] 0 = 30 µ M). Representing i D vs. n,

<!-- image -->

uncompetitive inhibition as per Equation (S25). Data analysis using nonlinear regression of this

equation allows for obtaining the value of

K

ୟ୮୮

୍మ

(

K

ୟ୮୮

୍మ

= 25.1 μM

(S28) (Table 4), which confirms the inhibition mechanism. (

B

) (

of

𝑖

ୈ

). Note the fulfilment of Equation

ሾIሿ

଴

=

50 µM) If the representation

vs. n gives rise to a hyperbola that does not pass through the origin of coordinates, it could

be a type (2) mixed inhibition with

ୟ୮୮

ୟ୮୮

ୟ୮୮

ୟ୮୮

K

ୟ୮୮

୍మ

< K

ୟ୮୮

୍భ

. The non-linear regression fit (

𝑖

ୈ

vs. n

), according

(Figure

େ

if a hyperbola is obtained that passes through the origin of coordinates, it could be an uncompetitive inhibition as per Equation (S25). Data analysis using nonlinear regression of this equation allows for obtaining the value of K app I2 (K app I2 = 25.1 µ M). Note the fulfilment of Equation (S28) (Table 4), which confirms the inhibition mechanism. ( B ) ( [ I ] 0 = 50 µ M) If the representation of i D vs. n gives rise to a hyperbola that does not pass through the origin of coordinates, it could be a type (2) mixed inhibition with K app I2 < K app I1 . The non-linear regression fit ( i D vs. n), according to Equation (S31), allows K app I1 and K app I2 to be determined, resulting in K app I1 (K app I1 = 31.5 µ M) and K app I2 ( K app I2 = 10.1 µ M ) . Note that these values satisfy Equation (S35) (see Table 4), which confirms the inhibition mechanism.

## 3. Material and Methods

## 3.1. Enzyme Source

Mushroom tyrosinase (3130 U/mg) was purchased from Merck Life (Madrid, Spain) and purified as previously described [53]. Protein content was determined by Bradford's method [54]. This enzyme is a tetramer with two heavy subunits, H, and two light ones, L [55].

## 3.2. Reagents

Benzoate, cinnamate and L-dopa were purchased from Merck Life (Madrid, Spain). Stock solutions of substrates were prepared in 0.15 mM phosphoric acid to prevent auto-oxidation.

## 3.3. Spectrophotometric Assays

Absorption was recorded in a visible-ultraviolet PerkinElmer Lambda 35-spectrophotometer (Perkin Elmer, Madrid, Spain), online interfaced with a compatible laptop. The temperature was maintained at 25 · C. Kinetics assays were also carried out with the above instruments by measuring the appearance of the products in the reaction medium. The activity on L-dopa was measured at 475 nm [56].

## 3.4. Simulation Assays

Initial rate (V D,DC 0 ) of the diphenolase activities in the absence (Scheme 1) and presence of different concentrations of inhibitor (Scheme 2) were calculated from the simulated progress curves obtained by numerical solution of the nonlinear set of differential equations corresponding to these mechanisms (see Supplementary Material). The systems of differential equations were solved numerically for particular sets of values of the rate constants and of initial concentrations of the species involved in the reaction mechanisms (WES) [57].

## 3.5. Kinetic Data Analysis

The initial velocity in the absence of inhibitor V D,DC 0 , and in the presence V D,DC o,i , were calculated by linear regression of the spectrophotometric recordings of the change in absorbance at 475 nm versus time. From these values, the degree of inhibition is determined:

i D % = ( V D,DC 0 -V D,DC o,i /V D,DC 0 ) × 100

Non-linear regression analysis [58] of the i D %values with respect to [ I ] 0 obtained at the same substrate concentration allows for obtaining the IC 50 . For each type of inhibition there is a relationship between IC 50 and the inhibition constant (competitive, non-competitive and uncompetitive) or constants (mixed). When the substrate concentration is varied, keeping the inhibitor concentration fixed, the non-linear regression analysis of the corresponding equation provides the values of K app I 1 : competitive inhibition, Equation (S17); K app I 2 : uncompetitive inhibition, Equation (S25); and both constant at mixed inhibition, Equation (S31).

The REFERASS computer program was used to obtain the rate equations of these mechanisms in the presence of inhibitor or of an alternative substrate [59].

## 3.6. Computational Docking

Molecular docking of the ligands was studied in the active site of mushroom tyrosinase. Their chemical structures were built from chemical structures obtained from the PubChem Substance and Compound database [60] (Table S1). The molecular structure of tyrosinase was taken from the Protein Databank (PDB ID:2Y9W, Chain A) [55], corresponding to the deoxy-form of tyrosinase from Agaricus bisporus . Input protein structure for docking was prepared by adding all hydrogen atoms and removing water molecules. The met and oxy forms of tyrosinase were built as previously described [61]. Gasteiger's partial charges and rotatable bonds were assigned by AutoDockTools4 software [62,63]. AutoDock 4.2.6 software package [63] was used for docking calculation. Lamarkian Genetic Algorithm was chosen to explore the space of active binding to search for the best conformers. Grid parameter files were built using AutoGrid 4.2.6 [64]. Other docking parameters were used as in [65]. PyMOL 2.3.0 (Schrödinger) was employed to build and inspect the molecule structures and docked conformations [66]. Docking conformations were selected from clusters of conformations that can lead to ligand catalysis with the lowest free energy of binding. Ligand-protein interactions were analysed using PLIP software [67].

## 4. Conclusions

The study of tyrosinase inhibition is very important due to the multiple applications it can have in pathological processes of pigmentation, such as the browning of fruits and vegetables. The importance of the IC 50 parameter and its quantitative relationships with the apparent inhibition constants are highlighted. Thus, from the IC 50 value, the inhibition constant for a competitive, non-competitive, or uncompetitive inhibitor can be determined when the inhibition mechanism is confirmed. In the case of mixed inhibition, the i D value obtained at different substrate concentrations is adjusted against n (n = [ D ] 0 /K D m ). Enzyme inhibition assays are discussed and some techniques for their optimization are proposed.

Supplementary Materials: The following supporting information can be downloaded at: https: //www.mdpi.com/article/10.3390/molecules27103141/s1. Scheme S1: Mechanism of action of tyrosinase on L-dopa in the presence of an alternative substrate (monophenol); Scheme S2: Mechanism of action of tyrosinase on L-dopa (D) in the presence of a suicide substrate (o-diphenol); Figure S1: Chemical structures of benzimidazothiazolone derivatives; Figure S2: Docking of (Z)-2-(4Hydroxybenzylidene)benzo[4,5]imidazo[2,1-b]thiazol-3(2H)-one to oxy-tyrosinase; Figure S3: Docking of (Z)-2-(3,4-Dihydroxybenzylidene)benzo[4,5]imidazo[2,1-b]thiazol-3(2H)-one to oxy-tyrosinase (A) and met-tyrosinase (B); Figure S4: Docking of (Z)-2-(2,4-Dihydroxybenzylidene)benzo[4,5]imidazo thiazol-3(2H)-one to oxy-tyrosinase; Figure S5: Chemical structures of urolithin derivatives: 1,3Dihydroxy-6H-benzo[c]chromen-6-one (a); 1,3-Dihydroxy-8-methoxy-6H-benzo[c]chromen-6-one (b) and 2'-(Hydroxymethyl)-[1,1'-biphenyl]-2,4-diol (c); Figure S6: Docking of 1,3-Dihydroxy-6H-benzo [c]chromen-6-one to oxy-tyrosinase; Figure S7: Docking of 1,3-Dihydroxy-8-methoxy-6H-benzo [c]chromen-6-one to oxy-tyrosinase; Figure S8: Docking of 2'-(Hydroxymethyl)-[1,1'-biphenyl]2,4-diol to oxy-tyrosinase; Figure S9: Chemical structure of a cinnamic acid derivative: Trans-3,4diflurocinnamic acid; Figure S10: Chemical structure of some indazoles: 7-bromo-1H-indazole (a); 6-bromo-1H-indazole (b); 4-chloro-1H-indazole (c); 6-fluoro-1H-indazole (d); 7-fluoro-1H-indazole (e); Figure S11: Chemical structure of benzoic acid derivatives: 2-amino benzoic acid (a); 4-amino benzoic acid (b); Figure S12: Chemical structure of luteolin; Figure S13: Docking of luteolin to oxytyrosinase; Figure S14: Docking of luteolin to met-tyrosinase; Figure S15: Chemical structure of propyl gallate; Figure S16: Chemical structure of polyphenols: sanggenone C (a); oxyresveratrol (b); L-epicatechin (c) and catechin (d); Figure S17: Docking of sanggenone C to oxy-tyrosinase; Figure S18: Docking of oxyresveratrol to oxy-tyrosinase; Figure S19A,B: Docking of L-epicatechin to oxytyrosinase (A) and met-tyrosinase (B); Figure S20A,B: Docking of catechin to oxy-tyrosinase (A) and met-tyrosinase (B); Figure S21: Chemical structure of phenetyl cinnamamide derivatives: N-transcaffeoyltyramine (a); N-trans-feruloyltyramine (b) and N-trans-coumaroyltyramine (c); Figure S22A,B: Docking of N-trans-caffeoyltyramine to oxy-tyrosinase (A) and met-tyrosinase (B); Figure S23: Docking of N-trans-feruloyltyramine to oxy-tyrosinase; Figure S24: Docking of N-trans-coumaroyltyramine to oxy-tyrosinase; Figure S25: Chemical structure of cinnamic acid ester derivatives: (E)-2-acetyl-5-

methoxyphenyl-3-(4-hydroxyphenyl)acrylate (a), (E)-2-isopropyl-5-methylphenyl-3-(4-hydroxyphenyl) acrylate (b) and (E)-2-acetyl-5-methoxyphenyl-3-(4-methoxyphenyl)acrylate (c); Figure S26: Docking of (E)-2-acetyl-5-methoxyphenyl-3-(4-hydroxyphenyl)acrylate to oxy-tyrosinase; Figure S27: Docking of (E)-2-isopropyl-5-methylphenyl-3-(4-hydroxyphenyl)acrylate to oxy-tyrosinase; Figure S28: Chemical structure of stilbenes: Strebluses C (a) and Strebluses D (b); Figure S29: Docking of Streblus C to oxy-tyrosinase; Figure S30: Docking of Streblus D to oxy-tyrosinase; Table S1: PubChem CID numbers correspond to the structure used to build the corresponding ligands; Table S2: Variation of i\_D to different [I]\_0 and [D]\_0=K\_mˆD; Table S3: i\_D values for [D]\_0=2K\_mˆD and [D]\_0=K\_mˆD; Table S4: Ligand-protein interactions observed in the docking conformations of the oxy and met forms of tyrosinase in the cases of competitive inhibition. Analysis of the interactions was carried out using PLIP software.

Author Contributions: J.L.M.-M., P.G.-M., F.G.-M. and F.G.-C. designed and directed the project and experiments. P.G.-M. performed all simulations experiments. P.G.-M. and F.G.-C. analysed and interpreted the results. P.G.-M., F.G.-M., J.A.T.-P., J.N.R.-L., F.G.-C. and J.L.M.-M., drafted the manuscript and figures, provided commentary and edits to the manuscript and figures, and prepared the final version of the article. All authors contributed to the article and approved the submitted version. All authors have read and agreed to the published version of the manuscript.

Funding: This work has been partially funded by Fundacion S é neca from Region de Murcia under the grant agreement (FS-RM) (20809/PI/18). J.L.M.-M. receive funding from internal grants in Northumbria University.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: Not applicable.

Conflicts of Interest: The authors declare no competing financial interest.

Sample Availability: Samples of the compounds described in Figure 2 are available from the authors.

## References

- 1. Kanteev, M.; Goldfeder, M.; Fishman, A. Structure-function correlations in tyrosinases. Protein Sci. 2015 , 24 , 1360-1369. [CrossRef] [PubMed]
- 2. S á nchez-Ferrer, Á .; Neptuno Rodr í guez-L ó pez, J.; Garc í a-C á novas, F.; Garc í a-Carmona, F. Tyrosinase: A comprehensive review of its mechanism. Biochim. Biophys. Acta Protein Struct. Mol. Enzymol. 1995 , 1247 , 1-11. [CrossRef]
- 3. Kim, K.; Huh, Y.; Lim, K.-M. Anti-Pigmentary Natural Compounds and Their Mode of Action. Int. J. Mol. Sci. 2021 , 22 , 6206. [CrossRef] [PubMed]
- 4. Maddaleno, A.S.; Camargo, J.; Mitjans, M.; Vinardell, M.P. Melanogenesis and Melasma Treatment. Cosmetics 2021 , 8 , 82. [CrossRef]
- 5. Zolghadri, S.; Bahrami, A.; Hassan Khan, M.T.; Munoz-Munoz, J.; Garcia-Molina, F.; Garcia-Canovas, F.; Saboury, A.A. Acomprehensive review on tyrosinase inhibitors. J. Enzyme Inhib. Med. Chem. 2019 , 34 , 279-309. [CrossRef]
- 6. Zhang, X.; Bian, G.; Kang, P.; Cheng, X.; Yan, K.; Liu, Y.; Gao, Y.; Li, D. Recent advance in the discovery of tyrosinase inhibitors from natural sources via separation methods. J. Enzyme Inhib. Med. Chem. 2021 , 36 , 2104-2117. [CrossRef]
- 7. Riaz, R.; Zucca, P.; Rescigno, A.; Peddio, S.; Saleem, R.S.Z.; Batool, S. Plants as a Promising Reservoir of Tyrosinase Inhibitors. Mini-Rev. Org. Chem. 2020 , 18 , 808-828. [CrossRef]
- 8. Peng, Z.; Wang, G.; Zeng, Q.-H.; Li, Y.; Liu, H.; Wang, J.J.; Zhao, Y. A systematic review of synthetic tyrosinase inhibitors and their structure-activity relationship. Crit. Rev. Food Sci. Nutr. 2021 , 1-42. [CrossRef]
- 9. Li, J.; Feng, L.; Liu, L.; Wang, F.; Ouyang, L.; Zhang, L.; Hu, X.; Wang, G. Recent advances in the design and discovery of synthetic tyrosinase inhibitors. Eur. J. Med. Chem. 2021 , 224 , 113744. [CrossRef]
- 10. Pillaiyar, T.; Manickam, M.; Jung, S.-H. Inhibitors of melanogenesis: A patent review (2009-2014). Expert Opin. Ther. Pat. 2015 , 25 , 775-788. [CrossRef]
- 11. Pillaiyar, T.; Namasivayam, V.; Manickam, M.; Jung, S.-H. Inhibitors of Melanogenesis: An Updated Review. J. Med. Chem. 2018 , 61 , 7395-7418. [CrossRef] [PubMed]
- 12. Molina, F.G.; Muñoz, J.L.; Var ó n, R.; L ó pez, J.N.R.; C á novas, F.G.; Tudela, J. An approximate analytical solution to the lag period of monophenolase activity of tyrosinase. Int. J. Biochem. Cell Biol. 2007 , 39 , 238-252. [CrossRef] [PubMed]
- 13. Ortiz-Ruiz, C.V.; Maria-Solano, M.A.; Garcia-Molina, M.D.M.; Varon, R.; Tudela, J.; Tomas, V.; Garcia-Canovas, F. Kinetic characterization of substrate-analogous inhibitors of tyrosinase. IUBMB Life 2015 , 67 , 757-767. [CrossRef] [PubMed]

- 14. Ujan, R.; Saeed, A.; Ashraf, S.; Channar, P.A.; Abbas, Q.; Rind, M.A.; Hassan, M.; Raza, H.; Seo, S.-Y.; El-Seedi, H.R. Synthesis, computational studies and enzyme inhibitory kinetics of benzothiazole-linked thioureas as mushroom tyrosinase inhibitors. J. Biomol. Struct. Dyn. 2021 , 39 , 7035-7043. [CrossRef]
- 15. Iraji, A.; Panahi, Z.; Edraki, N.; Khoshneviszadeh, M.; Khoshneviszadeh, M. Design, synthesis, in vitro and in silico studies of novel Schiff base derivatives of 2-hydroxy-4-methoxybenzamide as tyrosinase inhibitors. Drug Dev. Res. 2021 , 82 , 533-542. [CrossRef]
- 16. Yung-Chi, C.; Prusoff, W.H. Relationship between the inhibition constant (KI) and the concentration of inhibitor which causes 50 per cent inhibition (I50) of an enzymatic reaction. Biochem. Pharmacol. 1973 , 22 , 3099-3108. [CrossRef]
- 17. Cort é s, A.; Cascante, M.; C á rdenas, M.L.; Cornish-Bowden, A. Relationships between inhibition constants, inhibitor concentrations for 50% inhibition and types of inhibition: New ways of analysing data. Biochem. J. 2001 , 357 , 263-268. [CrossRef]
- 18. Lai, C.-J.; Wu, J.C. A Simple Kinetic Method for Rapid Mechanistic Analysis of Reversible Enzyme Inhibitors. Assay Drug Dev. Technol. 2003 , 1 , 527-535. [CrossRef]
- 19. Buker, S.M.; Boriack-Sjodin, P.A.; Copeland, R.A. Enzyme-Inhibitor Interactions and a Simple, Rapid Method for Determining Inhibition Modality. SLAS Discov. Adv. Life Sci. R D 2019 , 24 , 515-522. [CrossRef]
- 20. Rodr í guez-L ó pez, J.N.; Fenoll, L.G.; Peñalver, M.J.; Garc í a-Ruiz, P.A.; Var ó n, R.; Mart í nez-Ort í z, F.; Garc í a-C á novas, F.; Tudela, J. Tyrosinase action on monophenols: Evidence for direct enzymatic release of o-diphenol. Biochim. Biophys. Acta Protein Struct. Mol. Enzymol. 2001 , 1548 , 238-256. [CrossRef]
- 21. Rodr í guez-L ó pez, J.N.; Ros, J.R.; Var ó n, R.; Garc í a-C á novas, F. Oxygen Michaelis constants for tyrosinase. Biochem. J. 1993 , 293 , 859-866. [CrossRef] [PubMed]
- 22. Fenoll, L.G.; Rodr í guez-L ó pez, J.N.; Garc í a-Molina, F.; Garc í a-C á novas, F.; Tudela, J. Michaelis constants of mushroom tyrosinase with respect to oxygen in the presence of monophenols and diphenols. Int. J. Biochem. Cell Biol. 2002 , 34 , 332-336. [CrossRef]
- 23. Cornish-Bowden, A. Fundamentals of Enzyme Kinetics ; Portland Press: London, UK, 1995; ISBN 1855780720.
- 24. Segel, I.H. Enzyme Kinetics: Behavior and Analysis of Rapid Equilibrium and Steady State Enzyme Systems ; Irwin, H.S., Ed.; Wiley: Hoboken, NY, USA, 1975.
- 25. Copeland, R.A. Enzymes: A Practical Introduction to Structure, Mechanism, and Data Analysis , 2nd ed.; Wiley: Hoboken, NJ, USA, 2000; ISBN 978-0-471-35929-6.
- 26. Lee, S.; Choi, H.; Park, Y.; Jung, H.J.; Ullah, S.; Choi, I.; Kang, D.; Park, C.; Ryu, I.Y.; Jeong, Y.; et al. Urolithin and Reduced Urolithin Derivatives as Potent Inhibitors of Tyrosinase and Melanogenesis: Importance of the 4-Substituted Resorcinol Moiety. Int. J. Mol. Sci. 2021 , 22 , 5616. [CrossRef] [PubMed]
- 27. Chen, J.; Ran, M.; Wang, M.; Liu, X.; Liu, S.; Yu, Y. Structure-activity relationships of antityrosinase and antioxidant activities of cinnamic acid and its derivatives. Biosci. Biotechnol. Biochem. 2021 , 85 , 1697-1705. [CrossRef] [PubMed]
- 28. Öztürk, C.; Bayrak, S.; Demir, Y.; Aksoy, M.; Alım, Z.; Özdemir, H.; ˙ Irfan Küfrevioglu, Ö. Some indazoles as alternative inhibitors for potato polyphenol oxidase. Biotechnol. Appl. Biochem. 2021 . [CrossRef] [PubMed]
- 29. Gheibi, N.; Taherkhani, N.; Ahmadi, A.; Haghbeen, K.; Ilghari, D. Characterization of inhibitory effects of the potential therapeutic inhibitors, benzoic acid and pyridine derivatives, on the monophenolase and diphenolase activities of tyrosinase. Iran. J. Basic Med. Sci. 2015 , 18 , 122-129.
- 30. Lin, Y.-F.; Hu, Y.-H.; Lin, H.-T.; Liu, X.; Chen, Y.-H.; Zhang, S.; Chen, Q.-X. Inhibitory Effects of Propyl Gallate on Tyrosinase and Its Application in Controlling Pericarp Browning of Harvested Longan Fruits. J. Agric. Food Chem. 2013 , 61 , 2889-2895. [CrossRef]
- 31. Yin, Z.-H.; Li, Y.-F.; Gan, H.-X.; Feng, N.; Han, Y.-P.; Li, L.-M. Synergistic effects and antityrosinase mechanism of four plant polyphenols from Morus and Hulless Barley. Food Chem. 2022 , 374 , 131716. [CrossRef]
- 32. Sheng, Z.; Ge, S.; Xu, X.; Zhang, Y.; Wu, P.; Zhang, K.; Xu, X.; Li, C.; Zhao, D.; Tang, X. Design, synthesis and evaluation of cinnamic acid ester derivatives as mushroom tyrosinase inhibitors. Medchemcomm 2018 , 9 , 853-861. [CrossRef]
- 33. Jung, H.J.; Choi, D.C.; Noh, S.G.; Choi, H.; Choi, I.; Ryu, I.Y.; Chung, H.Y.; Moon, H.R. New Benzimidazothiazolone Derivatives as Tyrosinase Inhibitors with Potential Anti-Melanogenesis and Reactive Oxygen Species Scavenging Activities. Antioxidants 2021 , 10 , 1078. [CrossRef]
- 34. Nazir, Y.; Saeed, A.; Rafiq, M.; Afzal, S.; Ali, A.; Latif, M.; Zuegg, J.; Hussein, W.M.; Fercher, C.; Barnard, R.T.; et al. Hydroxyl substituted benzoic acid/cinnamic acid derivatives: Tyrosinase inhibitory kinetics, anti-melanogenic activity and molecular docking studies. Bioorg. Med. Chem. Lett. 2020 , 30 , 126722. [CrossRef] [PubMed]
- 35. Hashim, F.J.; Vichitphan, S.; Han, J.; Vichitphan, K. Alternative Approach for Specific Tyrosinase Inhibitor Screening: Uncompetitive Inhibition of Tyrosinase by Moringa oleifera. Molecules 2021 , 26 , 4576. [CrossRef] [PubMed]
- 36. Kim, J.K.; Heo, H.-Y.; Park, S.; Kim, H.; Oh, J.J.; Sohn, E.-H.; Jung, S.-H.; Lee, K. Characterization of Phenethyl Cinnamamide Compounds from Hemp Seed and Determination of Their Melanogenesis Inhibitory Activity. ACS Omega 2021 , 6 , 31945-31954. [CrossRef] [PubMed]
- 37. Nguyen, N.T.; Dang, P.H.; Nguyen, H.X.; Do, T.N.V.; Le, T.H.; Le, T.Q.H.; Nguyen, M.T.T. Tyrosinase Inhibitors from the Stems of Streblus Ilicifolius. Evid. Based Complementary Altern. Med. 2021 , 2021 , 5561176. [CrossRef]
- 38. Xie, L.-P.; Chen, Q.-X.; Huang, H.; Wang, H.-Z.; Zhang, R.-Q. Inhibitory Effects of Some Flavonoids on the Activity of Mushroom Tyrosinase. Biochemistry 2003 , 68 , 487-491. [CrossRef]

- 39. Zhang, L.; Zhao, X.; Tao, G.-J.; Chen, J.; Zheng, Z.-P. Investigating the inhibitory activity and mechanism differences between norartocarpetin and luteolin for tyrosinase: A combinatory kinetic study and computational simulation analysis. Food Chem. 2017 , 223 , 40-48. [CrossRef]
- 40. Kampatsikas, I.; Pretzler, M.; Rompel, A. Identification of Amino Acid Residues Responsible for C -HActivation in Type-III Copper Enzymes by Generating Tyrosinase Activity in a Catechol Oxidase. Angew. Chemie Int. Ed. 2020 , 59 , 20940-20945. [CrossRef]
- 41. Goldfeder, M.; Kanteev, M.; Isaschar-Ovdat, S.; Adir, N.; Fishman, A. Determination of tyrosinase substrate-binding modes reveals mechanistic differences between type-3 copper proteins. Nat. Commun. 2014 , 5 , 4505. [CrossRef]
- 42. Matoba, Y.; Oda, K.; Muraki, Y.; Masuda, T. The basicity of an active-site water molecule discriminates between tyrosinase and catechol oxidase activity. Int. J. Biol. Macromol. 2021 , 183 , 1861-1870. [CrossRef]
- 43. Garcia-Jimenez, A.; Munoz-Munoz, J.L.; Garc í a-Molina, F.; Teruel-Puche, J.A.; Garc í a-C á novas, F. Spectrophotometric Characterization of the Action of Tyrosinase on p-Coumaric and Caffeic Acids: Characteristics of o-Caffeoquinone. J. Agric. Food Chem. 2017 , 65 , 3378-3386. [CrossRef]
- 44. Garcia-Jimenez, A.; Garc í a-Molina, F.; Teruel-Puche, J.A.; Saura-Sanmartin, A.; Garcia-Ruiz, P.A.; Ortiz-Lopez, A.; Rodr í guez-L ó pez, J.N.; Garcia-Canovas, F.; Munoz-Munoz, J. Catalysis and inhibition of tyrosinase in the presence of cinnamic acid and some of its derivatives. Int. J. Biol. Macromol. 2018 , 119 , 548-554. [CrossRef] [PubMed]
- 45. Muñoz-Muñoz, J.L.; Garc í a-Molina, F.; Garc í a-Ruiz, P.A.; Molina-Alarc ó n, M.; Tudela, J.; Garc í a-C á novas, F.; Rodr í guez-L ó pez, J.N. Phenolic substrates and suicide inactivation of tyrosinase: Kinetics and mechanism. Biochem. J. 2008 , 416 , 431-440. [CrossRef] [PubMed]
- 46. Muñoz-Muñoz, J.L.; Garcia-Molina, F.; Varon, R.; Garcia-Ru í z, P.A.; Tudela, J.; Garcia-C á novas, F.; Rodr í guez-L ó pez, J.N. Suicide inactivation of the diphenolase and monophenolase activities of tyrosinase. IUBMB Life 2010 , 62 , 539-547. [CrossRef] [PubMed]
- 47. Ortiz-Ruiz, C.V.; Ballesta de los Santos, M.; Berna, J.; Fenoll, J.; Garcia-Ruiz, P.A.; Tudela, J.; Garcia-Canovas, F. Kinetic characterization of oxyresveratrol as a tyrosinase substrate. IUBMB Life 2015 , 67 , 828-836. [CrossRef]
- 48. Munoz-Munoz, J.L.; Garc í a-Molina, F.; Var ó n, R.; Tudela, J.; Garc í a-C á novas, F.; Rodr í guez-L ó pez, J.N. Generation of hydrogen peroxide in the melanin biosynthesis pathway. Biochim. Biophys. Acta Proteins Proteom. 2009 , 1794 , 1017-1029. [CrossRef]
- 49. Munoz-Munoz, J.L.; Garc í a-Molina, F.; Molina-Alarc ó n, M.; Tudela, J.; Garc í a-C á novas, F.; Rodr í guez-L ó pez, J.N. Kinetic Characterization of the Enzymatic and Chemical Oxidation of the Catechins in Green Tea. J. Agric. Food Chem. 2008 , 56 , 9215-9224. [CrossRef]
- 50. Chen, Q.-X.; Liu, X.-D.; Huang, H. Inactivation kinetics of mushroom tyrosinase in the dimethyl sulfoxide solution. Biochemistry 2003 , 68 , 644-649. [CrossRef]
- 51. Rodakiewicz-Nowak, J.; Ito, M. Effect of water-miscible solvents on the organic solvent-resistant tyrosinase from Streptomyces sp. REN-21. J. Chem. Technol. Biotechnol. 2003 , 78 , 809-816. [CrossRef]
- 52. Chen, C.-Q.; Li, Z.-C.; Pan, Z.-Z.; Zhu, Y.-J.; Yan, R.-R.; Wang, Q.; Yan, J.-H.; Chen, Q.-X. Inactivation kinetics of polyphenol oxidase from pupae of blowfly (Sarcophaga bullata) in the dimethyl sulfoxide solution. Appl. Biochem. Biotechnol. 2010 , 160 , 2166-2174. [CrossRef]
- 53. Rodr í guez-L ó pez, J.N.; Fenoll, L.G.; Garc í a-Ruiz, P.A.; Var ó n, R.; Tudela, J.; Thorneley, R.N.F.; Garc í a-C á novas, F. Stopped-Flow and Steady-State Study of the Diphenolase Activity of Mushroom Tyrosinase. Biochemistry 2000 , 39 , 10497-10506. [CrossRef]
- 54. Bradford, M.M. A rapid and sensitive method for the quantitation of microgram quantities of protein utilizing the principle of protein-dye binding. Anal. Biochem. 1976 , 72 , 248-254. [CrossRef]
- 55. Ismaya, W.T.; Rozeboom, H.J.; Weijn, A.; Mes, J.J.; Fusetti, F.; Wichers, H.J.; Dijkstra, B.W. Crystal Structure of Agaricus bisporus Mushroom Tyrosinase: Identity of the Tetramer Subunits and Interaction with Tropolone. Biochemistry 2011 , 50 , 5477-5486. [CrossRef] [PubMed]
- 56. Garc í a-Molina, F.; Muñoz, J.L.; Var ó n, R.; Rodr í guez-L ó pez, J.N.; Garc í a-C á novas, F.; Tudela, J. A Review on Spectrophotometric Methods for Measuring the Monophenolase and Diphenolase Activities of Tyrosinase. J. Agric. Food Chem. 2007 , 55 , 9739-9749. [CrossRef] [PubMed]
- 57. Garc í a-Sevilla, F.; Garrido-del Solo, C.; Duggleby, R.G.; Garc í a-C á novas, F.; Peyr ó , R.; Var ó n, R. Use of a windows program for simulation of the progress curves of reactants and intermediates involved in enzyme-catalyzed reactions. Biosystems 2000 , 54 , 151-164. [CrossRef]
- 58. Systat Software. Sigma Plot 9.0 for Windows ; Systat Software: San Jose, CA, USA, 2006.
- 59. Varon, R.; Garcia-Sevilla, F.; Garcia-Moreno, M.; Garcia-Canovas, F.; Peyro, R.; Duggleby, R.G. Computer program for the equations describing the steady state of enzyme reactions. Bioinformatics 1997 , 13 , 159-167. [CrossRef]
- 60. Kim, S.; Thiessen, P.A.; Bolton, E.E.; Chen, J.; Fu, G.; Gindulyte, A.; Han, L.; He, J.; He, S.; Shoemaker, B.A.; et al. PubChem Substance and Compound databases. Nucleic Acids Res. 2016 , 44 , D1202-D1213. [CrossRef]
- 61. Maria-Solano, M.A.; Ortiz-Ruiz, C.V.; Muñoz-Muñoz, J.L.; Teruel-Puche, J.A.; Berna, J.; Garcia-Ruiz, P.A.; Garcia-Canovas, F. Further insight into the pH effect on the catalysis of mushroom tyrosinase. J. Mol. Catal. B Enzym. 2016 , 125 , 6-15. [CrossRef]
- 62. Sanner, M.F. Python: A programming language for software integration and development. J. Mol. Graph. Model. 1999 , 17 , 57-61.
- 63. Morris, G.M.; Huey, R.; Lindstrom, W.; Sanner, M.F.; Belew, R.K.; Goodsell, D.S.; Olson, A.J. AutoDock4 and AutoDockTools4: Automated docking with selective receptor flexibility. J. Comput. Chem. 2009 , 30 , 2785-2791. [CrossRef]

- 64. Huey, R.; Morris, G.M.; Olson, A.J.; Goodsell, D.S. A semiempirical free energy force field with charge-based desolvation. J. Comput. Chem. 2007 , 28 , 1145-1152. [CrossRef]
- 65. Garc í a-Molina, P.; Garc í a-Molina, F.; Teruel-Puche, J.A.; Rodr í guez-L ó pez, J.N.; Garc í a-C á novas, F.; Muñoz-Muñoz, J.L. Considerations about the kinetic mechanism of tyrosinase in its action on monophenols: A review. Mol. Catal. 2022 , 518 , 112072. [CrossRef]
- 66. Schrödinger, L. The PyMOL Molecular Graphics System, V. 2.3. Available online: https://www.schrodinger.com/products/ pymol (accessed on 8 April 2022).
- 67. Adasme, M.F.; Linnemann, K.L.; Bolz, S.N.; Kaiser, F.; Salentin, S.; Haupt, V.J.; Schroeder, M. PLIP 2021: Expanding the scope of the protein-ligand interaction profiler to DNA and RNA. Nucleic Acids Res. 2021 , 49 , W530-W534. [CrossRef] [PubMed]