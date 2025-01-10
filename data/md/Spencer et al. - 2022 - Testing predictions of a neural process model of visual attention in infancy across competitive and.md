|

## RESEARCH ARTICLE

<!-- image -->

## Testing predictions of a neural process model of visual attention in infancy across competitive and non- competitive contexts

## John P./uni00A0Spencer 1

|

Shannon/uni00A0Ross- Sheehy

1 The University of East Anglia, Norwich, UK

2 University of Tennessee, Knoxville, USA 3 Florida International University, Miami, USA

## Correspondence

John P. Spencer, School of Psychology, 0.09 Lawrence Stenhouse Building, University of East Anglia, Norwich NR4 7TJ, UK.

Email: j.spencer@uea.ac.uk (J.P.S.)

Shannon Ross- Sheehy, 301G Austin Peay, 1404 Circle Drive, The University of Tennessee, Knoxville, TN 37996, USA. Email: rosssheehy@utk.edu (S.R.S.)

## Funding information

National Institute of Child Health and Human Development, Grant/ Award Number: F32HD055040 and R01HD083287

## Abstract

A key question in early development is how changes in neural  systems  give  rise  to  changes  in  infants'  behavior. We examine this question by testing predictions of a dynamic field (DF) model of infant spatial attention. We tested 5- , 7- , and 10- month- old infants in the Infant Orienting With Attention (IOWA) task containing the original  non- competitive  cue  conditions  (when  a  central stimulus disappeared before a cue onset) and new competitive cue conditions (when a central stimulus remained visible throughout the trial). This allowed testing of five model predictions: (1) that orienting accuracy would be higher and (2) reaction times would be slower for all competitive conditions; (3) that all infants would be slower to orient in the competitive conditions, though (4) older infants would show the strongest competition costs; and (5) that reaction times would be particularly slow for un- cued competitive conditions. Four of these five predictions were supported, and the remaining prediction was supported in part. We next examined fits of the model to the expanded task. New simulation results reveal close fits to the present findings after parameter modification.  Critically,  developmental  parameters  of the model were not altered, providing support for the DF model's account of neuro- developmental change.

This is an open access article under the terms of the Creative Commons Attribution- NonCommercial License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited and is not used for commercial purposes. © 2022 The Authors. Infancy published by Wiley Periodicals LLC on behalf of International Congress of Infant Studies.

|

2

<!-- image -->

|

Bret/uni00A0Eschman

3

|

<!-- image -->

## 1 | INTRODUCTION

Spatial information plays a key role in the early development of attention by providing a continuous dimension along which infants and children can relate to objects in the environment (Ross- Sheehy et al., 2015; Samuelson et al., 2011; Yuan et al., 2016). While infants' selective orienting of attention has been well documented on a behavioral level, the dynamics underlying its development and how they may shape early visual exploration of objects have been less studied (Ross- Sheehy et al., 2015). Here, we contribute to this literature using a neural process model to examine how the balance between holding central fixation and shifting attention to a peripherally appearing object changes in early development.

## 1.1 | Early development of spatial orienting

Attention  and  spatial  processing  systems  in  the  brain  develop  gradually  in  early  development as the indexing of spatial locations and shifts of attention- both covert and overt via eye movements- are integrated (Colombo, 2001; Corbetta et al., 2002; Katyal et al., 2010; Krauzlis et al., 2013; Petersen & Posner, 2012; Posner & Petersen, 1990). Evidence of change in this integration has been measured using spatial orienting tasks that have become a benchmark for the study of very early attention development. Prior work reveals that over the first year of life, infants  gradually  become faster  and  more  flexible  in  shifting  fixation  to  events  that  occur  in their peripheral visual field (Butcher et al., 2000; Hood & Atkinson, 1993; Johnson et al., 1991; Richards, 2005; Ross- Sheehy et al., 2015, 2020). Prior work also suggests covert orienting of attention, or attention to the peripheral visual field in the absence of an eye movement, modulates the speed and accuracy of later eye movements to a peripheral event (Kulke et al., 2016). Infants show reliable evidence of covert orienting by 12- 20/uni00A0weeks of age (Richards, 2000, 2001; Xie & Richards, 2017), and the development of covert orienting is driven by changes in the robustness of cortical responses in frontal and parietal regions before an eye movement to the target occurs (Richards, 2001, 2005). This could indicate that communication between brain regions involved in spatial processing and orienting of attention becomes more efficient with age.

Much of the literature has focused on neural mechanisms intrinsic to the child to better understand how spatial orienting changes. But how do different types of spatially relevant events influence covert orienting? Ross- Sheehy et al. (2015) tested covert and overt orienting with different types of cue/target relationships in the Infant Orienting With Attention (IOWA) task. In each type of trial, the aim was to measure the impact of a small dot (the cue) that appeared to the right or left of the infant's visual focus and that was paired with a tone, upon making a later eye movement toward a peripherally located target stimulus such as a photograph of an animal. Prior to the target presentation, infants were shown different types of cues along with the presentation of an auditory alerting tone. Valid cues appeared on the same side as a target and facilitated subsequent looks toward the target. Invalid cues  appeared on the side opposite from a target and interfered with subsequent looks toward the target. Double cues were two peripheral cues appearing simultaneously on the left and right, priming the infant to attend to a peripheral event without providing specific left/right spatial information. Tone cues contained only the auditory stimulus with a blank screen during the cueing period and alerted the infant to attend to upcoming events without providing spatial information. An additional control condition involved no cueing information (i.e., None ), and therefore, the target stimulus appeared without the infant's attention being manipulated beforehand.

|

<!-- image -->

Ross- Sheehy et al. (2015) tested 5- , 7- , and 10- month- old infants using the IOWA task and found that reaction times to shift to the peripheral target were faster overall for 10- month- old infants, followed by 7- month- olds, and then 5- month- olds, indicating that facility with shifting visual fixation improves with age. Differences across types of cues were also observed for each age group. Reaction times were fastest in conditions where the cue facilitated orienting to the target ( valid and double cue conditions) and slowest in conditions where the cue location interfered with the target (the invalid cue condition). Cues had the greatest impact on 7-  and 10- month- old infants, suggesting that covert orienting effects increase with age. The effects observed in this study using the IOWA task have further been replicated in recent studies (Ross- Sheehy et al., 2017, 2020).

## 1.2 | Early development and visual competition effects

The functional integration of attention and spatial processing must ultimately enable orienting to the most relevant events in environments with multiple objects. Experimentally, competition effects in visual orienting have been manipulated by presenting infants with a centrally located stimulus, followed by a peripheral stimulus that appears to the right or left while the central stimulus remains visible .  We refer to this as a competitive (sometimes referred to as an 'overlap') condition. Such conditions can be contrasted with what we refer to as non- competitive (sometimes referred to as 'gap') conditions where the central stimulus disappears before the peripheral target appears as in the IOWA task (Ross- Sheehy et al., 2015). Unlike non- competitive conditions, competitive conditions require that the infant disengages fixation from the stimulus on which they are focused to shift to a novel stimulus in a different region of the visual field. This ability relies on the activation of attention to a peripheral region of space and suppression of attention to competing stimuli (Amso & Scerif, 2015).

Differing neural activation when orienting with and without visual competition reveals that peripheral events may be less salient initially and that greater effort is required to shift fixation in the presence of a competing stimulus (Kulke et al., 2016, 2017, 2020). Even for adults, covert orienting toward a novel peripheral stimulus is diminished by the presence of an existing central stimulus, as evidenced by a smaller cortical response over parietal and occipital regions following the appearance of a peripherally located image (Kulke et al., 2016, 2020). This is consistent with other work showing that perception is enhanced for a peripheral stimulus within noncompetitive, as opposed to competitive, trials (Huestegge & Koch, 2010). For infants and adults, a larger response over the frontal cortex prior to shifting to a peripheral target suggests that visual competition requires greater effort to resolve (Kulke et al., 2016, 2017).

Although the speed with which infants are able to disengage from a persistent central stimulus and reorient to a peripheral stimulus increases from 1 and 6/uni00A0months of age (Butcher et al., 2000; Hood & Atkinson, 1993; Johnson et al., 1991; Kulke et al., 2015), all infants are slower to reorient attention in competitive conditions relative to non- competitive conditions (Butcher et al., 2000; Hood & Atkinson, 1993; Kulke et al., 2015). Further, infants' patterns of shifting in competitive contexts mature later than their orienting in non- competitive contexts (Matsuzawa & Shimojo, 1997).

Due to increasing lateralization of responses in infants' ERPs across the first year of life, it has been hypothesized that the ease of disengaging and shifting fixation from a familiar stimulus to a new one in infancy is enabled by more efficient interhemispheric coupling (Kulke et al., 2017). Given the relationship between orienting behaviors and early brain development, competition

|

<!-- image -->

effects have proven useful for studying individual differences in looking behavior (Frick et al., 1999). However, less is known about how orienting in these tasks may change in mid-  to late infancy, a time frame in which the cortical microstructure develops (Cao et al., 2017) and a number of cognitive skills emerge (Brune & Woodward, 2007; Cuevas & Bell, 2011). Further, a remaining experimental question is how the presence of visual competition modulates infants' covert orienting to various types of peripheral cues, such as those measured in the IOWA task.

## 1.3 | Applying neural process models

Although data indicate that improvements in cortical network efficiency are related to improvements in spatial orienting, it is often unclear precisely how changes in neural activity give rise to improvements in reaction times and accuracy of visual saccades. Neural process models can be a useful tool here, shedding light on precisely which type of neural changes give rise to behavioral effects observed in empirical studies. This is because neural models often implement known neurophysiological constraints, with individual model components representing different functional neuronal populations (e.g., perception, attention, saccade planning). In addition, connections within and between model components can be tuned to capture behavior in a neurally plausible way. Thus, these models can be especially useful in identifying how functional neural populations and network interactions impact behavior. Neural models can also be applied to inform developmental hypotheses about how the neural system changes over time. Such hypotheses are often implemented by making changes to model parameters to see whether these can explain the changes in behavior observed where we compare, for instance, data from younger and older infants in the same task.

Ross- Sheehy et al. then used the DF model to generate novel behavioral predictions. In particular, Ross- Sheehy et al. (2015) simulated infants' performance in a novel competitive variant of the IOWA task where there was visual competition between the continued presence of a fixation cue and the peripherally presented target. The model predictions for this competitive version of the IOWA task are shown in the solid lines in Figure 1; the simulated results from the original non- competitive version of the task are shown in dashed lines for comparison. Note that the top panels show simulation results for reaction times, while the bottom panels show percent correct saccades. Five novel predictions are evident in these simulations:

For example, in previous work, a dynamic field (DF) model comprised of a perceptual field, an attention field, and a saccade field was used to capture the detailed pattern of developmental changes in reaction times and accuracy reported by Ross- Sheehy et al. (2015). The model captured developmental changes in spatial orienting abilities by implementing the spatial precision hypothesis (SPH) that neural excitation and inhibition increase in strength in early development (Schöner et al., 2016; Schutte & Spencer, 2009; Schutte et al., 2003). Stronger local excitation increased the speed with which activation emerged following a peripheral visual cue, closely mimicking changes in covert attention observed in 5- , 7- , and 10- month- old infants. Moreover, visual competition effects over development were captured by increasing competitive interactions between fields through stronger long- range lateral inhibition. The model provided a good fit to the empirical data (i.e., the simulated values were within 12/uni00A0ms of the reaction time values across all age groups and within 4% of the accuracy data). This is important, giving us some confidence that the neural system implemented in the DF model accurately describes the neural processes that underlie infant orienting.

<!-- image -->

<!-- image -->

- 1.  Infant  reaction  times  should  be  slower  in  the  competitive  task.
- 3.  Infants should show diminished spatial cueing effects in the competitive task with the longest reactions times in no cue ( none ) condition.

|

- 2.  The slowing of reaction times in the competitive task should be more substantial for the older ages (7-  and 10- month- old infants).
- 4.  Diminished spatial cueing effects in the competitive task should also result in fewer errors for the invalid and double conditions, resulting in a higher accuracy for all ages.
- 5.  Accuracy should increase with age in the competitive task, meaning that older infants should be more likely to shift in the direction of the target even when the spatial cue was incongruent ( invalid cue) or ambiguous ( double cue).

## 1.4 | The current study

The first aim of the current study was to empirically test the five predictions derived from the Ross- Sheehy et al. (2015) DF model (henceforth referred to as the '2015 DF model'). To accomplish this, we modified the IOWA task to include the original non- competitive cue conditions (valid, invalid, double, tone only, and no cue) intermixed with competitive versions of the same five  conditions  in  which  the  central  fixation  stimulus  remained  visible  throughout  the  trial. This  design  allowed  us  to  make  within- subjects  comparisons  of  spatial  cueing  effects  when

FIGURE /one.LP Predictions of the 2015 DF model. These simulated data show non- competitive (dashed lines) and competitive (solid lines) versions of the IOWA task, separated by age group. Top panels show simulated model results for reaction times on correct trials, and lower panels show overall accuracy. Columns show results for 5-  (left), 7-  (middle), and 10- month- old (right) models across the differing cue conditions (for condition details, see text and Figures 2 and 3). Simulated results for the non- competitive task accurately captured empirical findings from Ross- Sheehy et al. (2015). Model predictions for the competitive task are tested in the current study

<!-- image -->

|

<!-- image -->

competition was absent (original non- competitive conditions) and when competition was present (new competitive conditions). The central question was whether empirical results were consistent with the five predictions of the 2015 DF model.

A second aim of this study was to examine whether the 2015 DF model could capture infants' performance from the current study without modifying the developmental parameters in the model. If possible, this would provide support for both the neural architecture implemented in the DF model, and the SPH account of development. To foreshadow our findings, empirical results from the competitive version of the task were generally consistent with the DF predictions; however, the quantitative results were not a close match to the simulated data in Figure 1. Thus, in  the  second  part  of  the  current  report,  we  examined  whether  the  2015  DF  model  could  be modified to quantitatively fit results from the current study without adjusting the developmental account proposed in that prior work.

## 2 | METHOD

## 2.1 | Participants

The final sample of infants recruited for the study included 84 infants, 43 tested in the United States, and 41 in the UK. The US infants included 19 5- month- old infants, ( M /uni00A0 =/uni00A0 168/uni00A0 days, SD /uni00A0 =/uni00A0 12/uni00A0 days),  15  7- month- old  infants  ( M /uni00A0 =/uni00A0 219/uni00A0 days, SD /uni00A0 =/uni00A0 17/uni00A0 days),  and  9  10- month- old infants ( M /uni00A0=/uni00A0303/uni00A0days, SD /uni00A0=/uni00A011/uni00A0days), 14/uni00A0girls, 29 boys, 4 unreported. An additional 22 infants were tested but were not included in the final sample due to equipment failure ( n /uni00A0 =/uni00A0 1),  or because they failed to meet the minimum data requirements for inclusion ( n /uni00A0 =/uni00A0 21).  The UK infants included 12 5- month- old infants ( M /uni00A0 =/uni00A0 152/uni00A0 days, SD /uni00A0 =/uni00A0 11.35/uni00A0 days),  12  7- month- old infants,  ( M /uni00A0 =/uni00A0 211/uni00A0 days, SD /uni00A0 =/uni00A0 18.90/uni00A0 days),  and  17  10- month- old  infants  ( M /uni00A0 =/uni00A0 305/uni00A0 days, SD /uni00A0 =/uni00A011.74/uni00A0days), 21/uni00A0girls, 20 boys. An additional 27 participants were tested by not included in the final sample due to experiment error/equipment failure ( n /uni00A0 =/uni00A0 13), fussiness or inattention ( n /uni00A0=/uni00A06), or failure to meet minimum data requirement for inclusions ( n /uni00A0=/uni00A08). Differences in attrition between sites were due to a greater rate of technical difficulties early in the data collection in the UK.

## 2.2 | Ethics statement

The  present  study  was  conducted  according  to  guidelines  laid  down  in  the  Declaration  of Helsinki, with written informed consent obtained from a parent or guardian for each child before any assessment or data collection. Data collection in the United States was reviewed and approved by an Internal Review Board (IRB) at the University of Iowa prior to the beginning of the experiment. Data collection in the UK was approved by an Ethics Committee within the School of Psychology.

## 2.3 | Stimuli and apparatus

During the experiment, infants were seated on a caregiver's lap in a dimly lit testing room 100/uni00A0cm away from a computer monitor on which the stimuli were presented. The caregiver was asked

|

<!-- image -->

to wear opaque sunglasses to eliminate any possibility that the infant might be influenced by indicators from their behavior. An online video recording was made of the infant's face during the experiment so that an experimenter could judge when the infant was looking to the central stimulus before beginning each trial. The same video recording was also used to later judge the timing and direction of eye movements offline.

All stimuli were presented against a light gray background. The stimuli and procedures in this study were identical to those used in the IOWA study (Ross- Sheehy et al., 2015; see Figure 2 for original IOWA stimuli, and Figure 3 for new competition conditions). Stimuli were presented on either a 37" (US) or 46" (UK) LCD. Visual angle was equated across laboratories, resulting in a viewable surface of 44.6° (w) by 25.9° (h). The central fixation stimulus was a smiley face that squished in shape and bounced from 2.4° (w) and 2.9° (h) to 4.1° (w) and 1.8° (h) at a rate of 1.5/uni00A0Hz. For the standard no competition trials, the smiley face disappeared at trial onset whereas for the competition trials, the smiley face became static on trial onset, and persisted throughout the trial. Peripheral cues were a small black circle (1° diameter) that was presented for 100/uni00A0ms at 11° to the right or left of the center of fixation. Target stimuli consisted of 52 GIFs of everyday items, such as an umbrella or a mailbox, 4.8° wide by 4.4° high, and also appeared 11° to the right or left of the center. An auditory tone (50/uni00A0Hz) was played through a centrally located speaker simultaneously with the presentation of the visual cue for all conditions except the no cue condition.

## 2.4 | Procedure

There were five possible cue conditions (double, invalid, none, tone, and valid) and competitive and non- competitive trial types, resulting in a total of ten experimental conditions (see Figures 2 and 3). Before each trial, the infant viewed a dynamic smiley face that squished and morphed in shape in the center of the screen. Once the observer judged that the infant was looking to the center of the monitor, a key was pressed to begin a trial. The smiley face would then disappear (in non- competitive trials)  or  become  static  (in  competitive  trials)  and  the trial would begin. The visual cue(s) and tone were then simultaneously presented for 100/uni00A0ms (except on 'tone' trials which had no visual cues and 'no cue' trials which had neither; see Figures 2 and 3). A brief 100- ms blank interval followed the presentation of the cue(s) and tone, followed by the presentation of the target stimulus either to the left or right of center. The observer then pressed a key to indicate the direction of the infant's first look, left or right. This keypress simultaneously ended the trial and initiated the next trial beginning with the central fixation stimulus. If no eye movement was made within 2,000/uni00A0ms following target presentation,  the  trial  automatically  ended  and  repeated.  Infants  continued  viewing  trials until they became bored or fussy or until they had completed over 80 trials. The experiment lasted, on average, about 10/uni00A0min.

## 2.5 | Design

The study had a cross- sectional, 3/uni00A0×/uni00A02/uni00A0×/uni00A05 design with age (5/uni00A0months, 7/uni00A0months, 10/uni00A0months) as a between- subjects factor, and competition (competitive, non- competitive) and cue type (double, invalid, none, tone, valid) as within- subjects factors. Each block contained one of every trial type (2 competition types/uni00A0×/uni00A05 cue types for a total of 10 trials per block) randomly presented. For each

|

FIGURE /two.LP The non- competitive conditions. A central fixation stimulus (the smiley face) squished and morphed in shape until the infant attended, followed by the presentation of a visual cue (the small black dot) paired with a tone, for 100/uni00A0ms. The screen was then blank for 100/uni00A0ms before the target stimulus (a picture of an everyday item) appeared. The target was presented until a look was made toward the right or left or until 2,000/uni00A0ms had passed. All of the conditions are shown, including valid trials in which the cue and target appeared on the same side of the monitor, invalid trials in which the cue and target appeared on opposite sides, and double cue trials in which two cues appeared simultaneously to the right and left. Baseline conditions include tone trials in which the spatially uninformative tone was played without a visual cue, and no cue trials with no visual cue and no auditory stimulus prior to the target presentation. This figure was reproduced from RossSheehy et al. (2015)

<!-- image -->

trial, dependent measures were infants' reaction times to look to the target (RT) and the proportion of trials in which they accurately looked toward the target (proportion correct). Trials in which the infant did not look away from the center were discarded from the analysis.

## 2.6 | Video coding

Video recordings were digitized at 30 fps and frame- by- frame coded to determine both direction of look and RT. Trials in which the infant's first look was toward the target were considered correct trials. These data were then used to calculate each infant's mean RT (correct trials only) and proportion correct for each condition (correct trials divided by total trials for each condition). The coders were blind to target location and experimental condition. Fifteen percent of the final sample was coded by a second coder to ensure accurate data processing. The coders agreed on the look onset within one video frame on 94% of trials.

## 2.7 | Statistical analysis

Because of the within- subject nature of our design, only infants that completed at least one correct  trial  in  each  condition  were  included in analysis. After applying this inclusion criterion, there were a few infants who only completed one or two correct trials in multiple conditions with fewer than 30 total trials completed (most infants completed >80 trials). Thus, we added a second criterion and excluded any infants who had completed fewer than 30 trials overall.

We analyzed our data using two mixed- design ANOVAs, one to examine infants' latency to orient to the target (reaction time), and the other to examine the accuracy of shifts to the peripheral target (proportion correct). For each of these ANOVAs, age was treated as a three- level betweensubjects factor (5, 7, and 10/uni00A0 months).  Competition  was  treated  as  a  two- level  within- subjects factor (competitive, non- competitive). Finally, cue type was treated as a five- level within- subjects factor (double, invalid, none, tone, and valid). Additionally, the country in which the data were collected (USA, UK) was included as a covariate in the analysis.

## 3 | RESULTS

## 3.1 | Reaction times to shift to the peripheral target

The top panels of Figure 4/uni00A0show the reaction time results. The most apparent finding is the striking difference in reaction times between the non- competitive and competitive conditions, with RTs drastically slowed during the competitive trials. A mixed- design ANOVA confirmed this observation,  revealing  a  significant  main  effect  of  competition, F (1,78)/uni00A0 =/uni00A0 196.618, p /uni00A0 </uni00A0 .001, /u1D702 2 p /uni00A0 =/uni00A0 .716, which was qualified by a significant age by competition interaction, F (2,78)/uni00A0=/uni00A03.643, p /uni00A0 =/uni00A0 .031, /u1D702 2 p /uni00A0 =/uni00A0 .085. As can be seen in Figure 5, older infants showed faster reaction times than 5- month- olds in the non- competitive conditions, but slower reaction times than 5- month- olds in the competitive conditions.

Finally, we found an interaction between competition and the country where the infants were tested, F (1,78)/uni00A0=/uni00A012.950, p /uni00A0 =/uni00A0.001, /u1D702 2 p /uni00A0 =/uni00A0.142. While all infants showed the same pattern in terms of the effect of competition, those tested in the United States were more affected by visual competition than those tested in the UK. Table 1/uni00A0summarizes the differences between these cohorts.

We also found a main effect of cue type, F (4,312)/uni00A0=/uni00A017.789, p /uni00A0</uni00A0.001, /u1D702 2 p /uni00A0=/uni00A0.186, and a cue type by competition interaction, F (4,312)/uni00A0 =/uni00A0 4.681, p /uni00A0 =/uni00A0 .001, /u1D702 2 p /uni00A0 =/uni00A0 .057.  Although  follow- up  simple main effects tests revealed significantly faster responding for all no competition conditions (all p s/uni00A0</uni00A0.001), the pattern of effects differed such that reaction times were longest in the invalid condition for the non- competitive trials, while reaction times were longest in the no cue ('none') condition for the competitive trials (see Figure 6).

## 3.2 | Proportion of correct saccades

Figure 4/uni00A0shows the proportion of correct trials for the non- competitive and competitive conditions. Once again, the effect of the competition is striking, producing markedly higher accuracy scores across all conditions. Cue type effects are also clearly visible, with lower accuracy for invalid and double cue conditions. A mixed- design ANOVA confirmed these observations, revealing both a significant main effect of competition, F (1,80)/uni00A0=/uni00A021.587, p /uni00A0</uni00A0.001, /u1D702 2 p /uni00A0=/uni00A0.212, and a signifi-

<!-- image -->

|

|

FIGURE /three.LP The competitive conditions. A central fixation stimulus (the smiley face) was presented throughout the entire trial. The smiley face squished and morphed in shape until the onset of the trial, and after that point, it was static. As in the non- competitive conditions, the cue and tone were presented for 100/uni00A0ms, followed by a 100- ms blank interval and then by the target stimulus. The target remained visible until a look was made to the right or left or until 2,000/uni00A0ms had passed

<!-- image -->

cant main effect of cue type, F (4,320)/uni00A0=/uni00A054.616, p /uni00A0 </uni00A0.001, /u1D702 2 p /uni00A0 =/uni00A0.406. We additionally found a significant  main  effect  of  age, F (2,80)/uni00A0 =/uni00A0 4.628, p /uni00A0 =/uni00A0 .013, /u1D702 2 p /uni00A0 =/uni00A0 .104,  with  10- month- old  infants demonstrating the highest accuracy rates overall. We also found three significant two- way interactions, including an age by competition interaction, F (2,80)/uni00A0=/uni00A03.792, p /uni00A0=/uni00A0.027, /u1D702 2 p /uni00A0=/uni00A0.087, an age by cue type interaction, F (8,320)/uni00A0=/uni00A04.196, p /uni00A0 </uni00A0 .001, /u1D702 2 p /uni00A0 =/uni00A0 .095, and a competition by cue type interaction, F (3,320)/uni00A0=/uni00A016.915, p /uni00A0</uni00A0.001, /u1D702 2 p /uni00A0=/uni00A0.175.

However, all of these effects were subsumed under a significant three- way age by competition by cue type interaction, F (8,156)/uni00A0=/uni00A02.224, p /uni00A0=/uni00A0.026, /u1D702 2 p /uni00A0=/uni00A0.053. As can be seen in Figure 4, this interaction was driven primarily by relatively large cue effects and relatively low accuracy for the 7- month- old infants compared with both the 5-  and 10- month- old infants. To examine this further, simple main effects of age for each cue type were examined for both the no competition and competition conditions. Results revealed significant age effects only for the invalid ( p /uni00A0=/uni00A0.014) and double cue ( p /uni00A0 =/uni00A0 .005) no competition conditions; competition conditions did not differ by age. Additional pairwise comparisons (Bonferroni corrected for multiple comparisons) revealed that 7- month- old infants were significantly less accurate than 10- month- old infants in the double cue no  competition  condition  ( p /uni00A0 =/uni00A0 .015),  and  significantly  less  accurate  than  both  5- month- old ( p /uni00A0=/uni00A0.014) and 10- month- old infants ( p /uni00A0=/uni00A0.014) in the invalid no competition condition.

|

FIGURE /four.LP Infant data from the behavioral study. Infant data for non- competitive (dashed lines) and competitive (solid lines) versions of the IOWA task, separated by age group. Top panels show infants' reaction times on correct trials, and lower panels show overall accuracy. Columns show results for 5-  (left), 7-  (middle), and 10- month- old (right) infants across the differing cue conditions (for condition details, see text and Figures 2 and 3). Cue types are indicated along the x - axis. Error bars show the mean standard error

<!-- image -->

## 4 | DISCUSSION

The goal of this study was to examine developmental differences in spatial attention across visually competitive contexts in order to test five novel behavioral predictions of a DF model of spatial attention and orienting. Most of these predictions were supported. In particular, reaction times were dramatically slowed in the competitive conditions (Prediction 1), with a larger slowing of reaction times for the older infants (Prediction 2). The first part of Prediction 3 that there would be a 'flattening' of the reaction time effects across conditions in the competitive conditions was not supported by these results. Instead, a cue type by competition interaction revealed that differing patterns of cueing effects were present between visually competitive and non- competitive trials. However, the prediction made by the model that the longest reaction times would be found in the no cue (none) condition during competition was supported by the data. Regarding accuracy, infants showed an overall improvement in accuracy in the competitive conditions (Prediction 4). Moreover, there was an age effect in the non- competitive conditions, but not in the competitive conditions; thus, there was a larger improvement in accuracy for the older children as a result of visual competition (Prediction 5).

Although there was support for all five model predictions, the quantitative predictions of the DF model (see Figure 1) were inaccurate in specific ways. In particular, reaction times in the competitive conditions were much slower than predicted by the model. Similarly, the model  showed  a  larger  improvement  in  accuracy  in  the  competitive  conditions  than  was evident in the data. These discrepancies are likely a result of task differences between the

|

5

FIGURE /five.LP Competition by age group interaction. The graph shows differences in mean reaction times between the non- competitive (dashed line) and competitive (solid line) conditions for 5- month- old (left), 7- month- old (middle), and 10- month- old infants (right). Error bars show the mean standard error

<!-- image -->

s

h

t

n

o

m

0

1

s

h

t

n

o

m

7

s

h

t

n

o

m

hypothesized competition variant of the IOWA task implemented in the 2015 DF model, and the actual task subsequently developed. Thus, in next section, we explored whether model parameters could be adjusted to provide a better quantitative fit to the new task, while maintaining good quantitative fits for the original IOWA task. As mentioned previously, a key aim was to determine whether a quantitative fit could be achieved without modifying the developmental parameters in the DF model. If the age parameters within the 2015 DF model generalize to the new data, it would provide support for the neuro- developmental mechanisms specified in the DF model.

## 5 | A DF MODEL OF INFANT ORIENTING AND ATTENTION

The DF model was reported in full detail in Ross- Sheehy et al. (2015). Thus, we provide a cursory overview here and then focus on simulations of the present data set. The model consists of an attention field, a saccade motor field, and three control nodes that help regulate the fixation state, a gaze change state, and the resetting of the cortical fields following a saccade (see Figure 7).

Visual input to the model (Figure 7a, top layer) is entered directly to the attention field (Figure 7a, middle layer)- a continuous spatial dimension that captures the spatial position of items in the foveal and peripheral visual field. In the model, we use a single horizontal dimension reflecting the left, center, and right positions of items in the display. The size of each object is scaled to reflect the size of the stimuli in the experiment, and the timing of the stimuli mimics the events

|

<!-- image -->

FIGURE /six.LP Competition by cue type interaction. The graph shows differences in mean reaction times between the non- competitive (dashed line) and competitive conditions (solid line) across the different cue types ( x - axis). Error bars show the mean standard error

<!-- image -->

TABLE /one.LP Competition effects by country of testing

|    | Non- competitive conditions   | Non- competitive conditions   | Competitive conditions   | Competitive conditions   |
|----|-------------------------------|-------------------------------|--------------------------|--------------------------|
|    | Mean RT (ms)                  | SE                            | Mean RT (ms)             | SE                       |
| US | 257.43                        | 4.81                          | 428.69                   | 15.63                    |
| UK | 283.78                        | 5.55                          | 389.61                   | 10.32                    |

in the non- competitive and competitive conditions. Long- range inhibition in the attention field ensures that only one region of the field is able to support a robust attention 'peak.' Thus, there is only one focus of attention at a time.

There are two additional parts of the neural architecture. A fixation node (see Figure 7a) receives input from stimuli in the fovea. When this node goes above threshold into an 'on' state, it raises the activation level in the attention field around the fovea, helping to stabilize fixation. A second gaze change node (see Figure 7b) receives input from the tone cue. This is an orienting cue

Once a peak has formed in the spatial attention field, this field passes activation to a saccade motor field (see bottom layer in Figure 7a) to guide the formation of a motor plan for an eye movement to the attended location. The spatial attention field does not project to the saccade field around the fovea; thus, if the model is currently fixating a stimulus, no eye movement is generated. Peripheral peaks, however, will project activation to the saccade motor field with the size of the eye movement scaled to the distance from the center. Finally, a reset node (Figure 7d) globally inhibits activation in all parts of the neural system during the eye movement.

|

Fixa/g415on (A), Cue (B), Target Presenta/g415on (C), and Saccade Ini/g415a/g415on (D) on No Compe/g415/g415on Trial

<!-- image -->

Cue (E) and Target (F) Presenta/g415on on Compe/g415/g415on Trial

<!-- image -->

FIGURE /seven.LP Neural processes that underlie performance of the present DF model. Panels a- d show the model in the invalid condition of the non- competitive task. Panels e- f (blue rectangle) show the model during the cue (e) and target presentation (f) in the competitive task. The top layer in each panel shows the horizontal input (the white region indicates input size). The second layer in each panel shows the attention field. The blue line shows activation ( y - axis) over the horizontal spatial dimension ( x - axis) with 0 at the fovea. The green line shows the input to the attention field (which mimics the top layer). The two triangles near the fovea show the fixation node (above threshold in a) and the gaze change node (above threshold in b). Lower layers show the saccade motor field. Different panels show the following events: fixation stimulus (a), cue presentation (and no fixation stimulus) (b), target presentation (c), saccade peak formation (d), cue presentation (and continued fixation input) in the competitive task, target presentation (and continued fixation input) in the competitive task. Red ovals highlight activation differences during cue and target presentation in the non- competitive and competitive task (see text for details)

that indicates that an attention cue is being presented in the periphery. When the gaze change node goes above threshold into an 'on' state, it raises the resting excitatory level outside of the fovea,  helping  to  induce  an  attention  peak  in  the  periphery.  Note  that  the  fixation  and  gaze change nodes are mutually inhibitory.

Figure 7/uni00A0 shows  how  activation  in  the  DF  model evolves during events in non- competitive (Figure 7a- d) and competitive (Figure 7e- f) conditions. The first event in the task is the presentation of the fixation stimulus. This leads to the formation of a robust fixation peak in the attention field and drives the fixation node into the 'on' state (Figure 7a). Next, the fixation stimulus is removed and a peripheral cue and tone are presented (Figure 7b). In this case, an invalid cue is presented which builds above- threshold activation on the left of the attention field. The tone facilitates this activation by driving the gaze change node into the 'on' state. Because the peripheral cue is small and short- lived, activation on the left side of the attention field is not sufficient to form a peak in the saccade motor field. Nevertheless, the attention peak on the left of the field competes with the emerging activation on the right side of the attention field when the target is presented (Figure 7c). This slows down the formation of the attention peak toward the target when the cue is invalid. Eventually, however, a peak forms in the saccade motor field (Figure 7d), driving an eye movement to the target. As with infants, the time at which the eye

|

<!-- image -->

<!-- image -->

movement is initiated determines the reaction time and the direction relative to the target determines its accuracy.

To capture developmental changes in performance in prior work, parameter settings were varied such that interactions within and between neural fields were stronger with increasing age. These changes were based on the spatial precision hypothesis - that excitatory and inhibitory interactions in cortical fields become stronger and more efficient with development (Perone et al., 2011; Ross- Sheehy et al., 2015; Schutte & Spencer, 2009; Schutte et al., 2003; Spencer et al., 2007). Four developmental parameter changes were implemented in the model: (1) The strength of excitation, local inhibition, and global inhibition in the attention field was increased over ages; (2) the strength of excitation and global inhibition in the saccade motor field was increased over ages; (3) the strength of the projection from the attention field to the saccade motor field was increased over ages; and (4) the noise level in the attention and saccade motor fields was reduced over ages. These changes effectively reproduced differences in reaction times and proportion correct over development reported by Ross- Sheehy et al. (2015) with a good overall quantitative fit to the data. On average, the model reproduced the reaction times within ~12/uni00A0ms of the empirical values and within 4% of the accuracy value.

The final two panels in Figure 7 show the cue (Figure 7e) and target (Figure 7f) presentation events in the competitive conditions. Notice that the fixation stimulus remains 'on' during these events, biasing the model to remain fixated at the center due to the robust fixation peak competing with cue presentation. This reduces the impact of the cue, with weaker activation at this peripheral location in the competitive conditions (compare red oval in Figure 7e to red oval in 7b). Similarly, the fixation peak competes with the target presentation, leading to a slowing of activation growth when the target is presented and longer reaction times (compare red oval in Figure 7f to red oval in 7c).

## 5.1 | Modifications to original model and simulation methods

The difference between the non- competitive and competitive conditions is the continued presence of the fixation stimulus in the latter task. Conceptually, this should impact activation at the fovea in the attention field as well as the activation of the fixation node that biases the model to sustain attention toward the center. In the previous model, no input was provided to the fixation node given that there was no competition present. Thus, the model was updated to include an input to this node that occurred whenever the central stimulus was on.

After modifying these parameters, the model showed a balance between entering the fixation state and the gaze change state that was more consistent with that of the data; however, the model often had two peaks- a fixation peak and a target peak- simultaneously. This violated the nature of the attention field which should only have one robust focus of attention at a time. Scaling the global inhibition parameters by 1.95 restored this constraint. Note that global

Given that the fixation node now received direct input, its parameters were adjusted, including the strength of input from the stimulus to the fixation node, and the strength of self- excitation within the internal dynamics of the node. Moreover, because the fixation node and gaze change node are mutually inhibitory, this required that the self- excitation of the gaze change node was changed (because the gaze change node was now receiving inhibition from the fixation node, we had to boost excitation to compensate). The final parameters for the fixation node were as follows: (1) fixation self- excitation/uni00A0=/uni00A05.0, (2) gaze change self- excitation/uni00A0=/uni00A02.5, (3) mutual inhibition/uni00A0=/uni00A01.0, and (4) input strength to fixation node/uni00A0=/uni00A07.

|

Figure 8/uni00A0 shows findings from the simulations (open circles, gray lines) relative to the empirical data (filled in circles, red lines) for the 5- month- old infants (left), the 7- month- old infants (middle), and the 10- month- old infants (right). Across all three age groups, the model closely captured infants' reaction times within the no competition conditions (dashed lines in top panels). Reaction times in the competition conditions (solid lines in top panels) were captured less robustly, with the model showing faster RTs for the 5- month- old infants, slower RTs for the 7- month- old infants, and a close quantitative fit for the 10- month- old infants.

<!-- image -->

inhibition was modulated by age in the previous model. It is important to highlight that the same scaling parameter was used for all ages here.

Using the revised model, we ran 400/uni00A0simulations of the cue conditions within the no competition  and  competition versions of the task for each age group. Like the behavioral study, dependent variables included reaction times to shift to the target (measured as the time step during which a saccade is initiated), and the proportion of saccades that occurred to the target side. As in our previous report, an additional 75/uni00A0ms was added to the reaction time of each saccade to account for the motor response (Ross- Sheehy et al., 2015). We ran a replication set of simulations to verify that the final parameters were robust to noise. This was the case: Overall root mean squared error (RMSE) for the replication set was 37.9/uni00A0ms for reaction times and 0.07 for accuracy. Note that all simulation code and results are available at https://github.com/cosiv ina/cosiv ina\_dft\_projects.

Two additional parameter changes were included in the final simulations reported below. Initial simulation results showed relatively few errors in response to the invalid and double cues in the competitive conditions. To boost the error rate, we modeled an increase in the salience of the cue input by increasing the cue size from 10 to 17. We also added a scaling parameter to the noise in the attention field, multiplying the noise strength by 2.0. The developmental changes in noise remained the same as in the previous model.

## 5.2 | Simulation results and discussion

We quantified these model fits by computing the root mean squared error (RMSE)- a commonly used metric to evaluate model accuracy- for each age group across no competition and competition conditions for both RTs and accuracy (see Table 2). For context, we also computed RMSE values using the 2015 DF model from Ross- Sheehy et al. (note that the RMSE values computed using the data in Figure 8 are referred to as the '2021/uni00A0Model' in Table 2). As can be seen in Table 2, the 2015/uni00A0Model provided a close overall fit for accuracy and for RTs from the no competition conditions, but this model did not provide an accurate account of RTs from the competition conditions. The new model provided a far better quantitative fit to the RTs from both no competition and competition conditions, with an overall RMSE of 15.9/uni00A0ms and 48.3/uni00A0ms respectively. On average, then, the 2021/uni00A0Model values are within 37/uni00A0ms of the empirical data. Importantly, the closer RT fit was achieved while still fitting to infants' rates of accuracy. Indeed, the 2021/uni00A0Model shows accuracy below 0.10 for all conditions and for all age groups; in this way, the accuracy results are more stable overall relative to the 2015/uni00A0Model, even though the overall RMSE value is

Quantitative results for the accuracy data are shown in the lower panels of Figure 8. Accuracy fits for the 5- month- old infants were good in both the no competition (dashed lines) and competition conditions (solid lines). For the older infants, the model showed balanced accuracy results for the no competition conditions, with fewer errors for the 7- month- old infants and more errors for the 10- month- old infants.

|

<!-- image -->

FIGURE /eight.LP The final simulations overlaid with the present empirical data. Reaction times during correct trials (top panel) and rates of accuracy (bottom panel) are shown for the non- competitive (dashed lines) and competitive (solid lines) conditions. The left panel shows 5- month- old data and simulations, the middle panel shows 7- month- old data and simulations, and the right panel shows 10- month- old data and simulations. Empirical results are shown in red with filled in circles, while model simulations are shown in gray with open circles

<!-- image -->

TABLE /two.LP Root Mean Squared Errors (RMSE) between the infant data and the 2015 versus 2021 DF models

|                    |                | Root mean squared error (RMSE)   | Root mean squared error (RMSE)   | Root mean squared error (RMSE)   | Root mean squared error (RMSE)   |
|--------------------|----------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|
|                    |                | 5/uni00A0months                  | 7/uni00A0months                  | 10/uni00A0months                 | Overall                          |
| 2015/uni00A0Model  |                |                                  |                                  |                                  |                                  |
| Reaction time      | No competition | 24.1                             | 17.2                             | 38.7                             | 26.7                             |
|                    | Competition    | 114.5                            | 110.1                            | 140.6                            | 121.7                            |
| Proportion correct | No competition | 0.02                             | 0.01                             | 0.12                             | 0.05                             |
|                    | Competition    | 0.06                             | 0.1                              | 0.06                             | 0.07                             |
| 2021/uni00A0Model  |                |                                  |                                  |                                  |                                  |
| Reaction time      | No competition | 11.7                             | 7.6                              | 28.3                             | 15.9                             |
|                    | Competition    | 61.8                             | 52.1                             | 30.8                             | 48.3                             |
| Proportion correct | No competition | 0.03                             | 0.08                             | 0.09                             | 0.07                             |
|                    | Competition    | 0.06                             | 0.09                             | 0.06                             | 0.07                             |

slightly higher in the no competition condition for the 2021/uni00A0Model. In summary, the 2021/uni00A0Model provides a good overall quantitative fit, particularly given that relatively few parameters were modified relative to the previous report.

|

<!-- image -->

Because some differences were found between our results and prior work (Ross- Sheehy et al., 2015), for instance, 7- month- olds showed lower rates of accuracy in the no competition trials here, some of the ways in which the model fits were not an exact fit to the present data reflect subtle variability between studies. This is reflected in the RMSE values: In Ross- Sheehy et al. (2015), we reported RMSE values of 12/uni00A0ms for RTs and 0.04 for accuracy; the same model fit to the no competition data reported here had an accuracy of 26.7/uni00A0ms for RTs and 0.05 for accuracy. These differences could be due to infants completing a more difficult task with competitive and non- competitive versions of every cue condition randomized within each block, and the lower power/higher levels of noise that resulted from twice the number of experimental conditions. While the model's behavior is consistent regardless of the number of experimental conditions, infants may complete fewer trials per condition before they become tired.

A second challenge in modeling these data relative to the previous data is the number of within- subjects variables to capture. Consider, for instance, the accurate performance of the 7and 10- month- old models in the competitive double and invalid conditions. We could increase errors  in  these  conditions  by  increasing  the  strength  of  the  cue  in  the  model.  When  we  did this,  however, overall RMSE for accuracy increased because this increased errors in the noncompetitive conditions as well. It is likely we could counteract this by changing the developmental parameters for specific age groups; however, we opted for the more constrained approach to parameter tuning described above that did not modify the developmental parameters within the model.

## 6 | GENERAL DISCUSSION

Presented here are results from two converging lines of work that examined the developmental origins of spatial attention and visual competition effects in infancy. The first line of work contains behavioral findings from a competitive version of the IOWA task, a novel modification of the original IOWA task that included both no competition trials and competition trials. The second line of work contains simulations from a DF model that has been adapted to capture the details of infant orienting behaviors under varying degrees of visual competition. Both lines of work replicate and extend previous findings (Ross- Sheehy et al., 2015), allowing us to then look more closely at mechanisms of competition effects in infancy, that is, the tendency to orient more slowly to peripherally located targets when there are multiple objects in the visual field (Butcher et al., 2000; Hood & Atkinson, 1993; Johnson et al., 1991; Kulke et al., 2015). Although most explanations of the competition effect suggest developmental improvements in attention 'disengaging,' we show here that these effects can be captured without invoking developmental changes in an explicit disengagement mechanism.

The behavioral findings replicated previous research (Ross- Sheehy et al., 2015) and further revealed classic gap- overlap effects in the newly introduced competitive conditions. As in previous research, infants were fastest and most accurate for the valid, non- competitive conditions in which an earlier cue and later target appeared on the same side, and slowest and least accurate for the invalid, non- competitive conditions in which the cue and target appeared on opposite sides. In addition to these robust spatial cueing effects, competition from the persistent fixation stimulus dramatically increased reaction times toward the target, regardless of age. Interestingly, however,  this  competition  effect  was  most  pronounced  for  the  older  infants:  10- month- olds showed an average competition cost of 151.75/uni00A0ms and 7- month- olds showed a cost of 145.96/uni00A0ms, whereas 5- month- olds showed substantially lower competition costs of 112.55/uni00A0ms (see Figure

|

<!-- image -->

- 5). This finding is somewhat counterintuitive as younger infants typically have more difficulty resolving visual competition than older infants (Cousijn et al., 2017; Saez de Urabain et al., 2017).

Thus, the DF model offers a parsimonious explanation encompassing both the decrease in reaction times over age in the no competition conditions and the increase in reaction times over age in competition conditions with the same developmental parameters. The developmental story itself is relatively simple and biologically plausible- increase the strength of excitation and inhibition over development. We note that such changes are likely an outcome of simple Hebbian learning, producing changes in the strength of excitatory and inhibitory interactions that result in the complex pattern of development reported here.

Critically, the DF model captured these developmental increases in competition costs via a unified account of change, where neural interactions get stronger from 5 to 10/uni00A0months. In the no competition conditions, stronger neural interactions speed up reaction times overall, but also accentuate the cost of the cue in the conditions with invalid cue locations (i.e., we see a bigger difference between responses following valid versus invalid cues). In the competition conditions, the stronger neural interactions make it harder to release fixation from the central stimulus, so we see an overall increase in reaction times, particularly in the no tone condition when there is no orienting input to help overcome the fixation stimulus.

In addition to these age- related competition effects, we noted condition effects that varied by competition. In particular, although reaction times for no competition trials were faster for neutral or congruent spatial cues (Figure 8), this was not the case for competition trials; all cues, regardless of spatial congruence, facilitated/uni00A0faster latencies in the competition conditions compared to the no cue baseline condition. The observed interactions between competition and cue type were originally predicted by the 2015 DF model, though the effect in the data was greater than predicted. Further, although spatial congruence impacted infants' reaction times during competitive conditions, the effect was relatively subtle compared to the no competition conditions. In the model, for both competition and no competition conditions, the tone cue serves as a general orienting cue, driving the gaze change node. However, in the context of visual competition, reaction times slow down and there is an emergent re- ordering of the condition effects as the cue, the tone, and the fixation cue all balance one another out. Importantly, no explicit re- weighting of cues is required across non- competitive and competitive conditions.

Results for accuracy measures also replicated previous findings demonstrating developmental increases in error rates as a result of covert orienting toward peripheral cues. Ross- Sheehy et al. (2015) reasoned that this counterintuitive effect may have been driven by particularly fast reaction times for the oldest infants. By the time a target appeared, older infants may have already reached a point- of- no- return in saccade programming toward the location of the cue. This essentially resulted in a speed/accuracy trade- off. As reaction times decreased, so too did accuracy. Based on that prior observation, we predicted that competition effects from the centrally located stimulus should decrease older infants' error rates because infants would take more time to shift in general. Current findings demonstrate marked accuracy improvements across all competition conditions and all age groups, with older infants showing the greatest improvement. The model also captured these trends qualitatively, but consistently produced fewer errors compared with infants in the competition conditions with double and invalid cues. Simulation work demonstrated that it was possible to increase the error rate in the competitive conditions, but at a cost of increased errors in the non- competitive conditions. It is likely possible to balance these effects with additional tuning of the developmental parameters. We did not pursue this here because the fit of the model was reasonably good without this additional tuning.

|

<!-- image -->

Developmental changes in the model arise through implementation of the/uni00A0 spatial precision hypothesis (SPH; Schöner/uni00A0et al., 2016; Schutte & Spencer, 2009; Schutte et al., 2003),/uni00A0which posits that/uni00A0 increased efficiency/uni00A0of excitatory and inhibitory/uni00A0interactions/uni00A0within neural networks may give rise to developmental improvements, such as more efficient orienting to peripheral stimuli (Ross- Sheehy et al., 2015)./uni00A0The SPH was also used here to capture competition- driven trade- offs, as well as age- driven differences, in/uni00A0the/uni00A0accuracy of visual shifts. To the best of/uni00A0our knowledge, these results are the first to incorporate both reaction time/uni00A0 and /uni00A0 accuracy measures in assessing visual competition effects. Contrary to the typical characterization of visual competition as an/uni00A0impediment to an otherwise nimble reflexive orienting system, we show here that visual competition may also incur benefit/uni00A0by/uni00A0suppressing distracting information in the visual field,/uni00A0increasing accuracy to shift toward the more enduring stimulus for all age groups and particularly for 7- month- old infants.

Future work could also clarify how the mechanisms presented here relate to other aspects of visual attention in infancy. For example, learning about sequences of events in the infants' environment likely plays a role in anticipating and programming looks to peripheral events prior to their occurrence (Wentworth & Haith, 1998). Also, the top- down input from the frontal eye fields and the dorsolateral prefrontal cortex are likely to be more multifaceted than the mechanisms captured here (Fan et al., 2005; Johnson et al., 1991). Exploring these mechanisms further may provide insight into those processes required to disengage from the current focus of attention (Johnson & De/uni00A0Haan, 2015).

A key future question is how the architecture and neural dynamics of the DF model relate to  neural  population  activity  in  the  developing  brain.  For  instance,  the  competition  effects demonstrated in the model are predominately driven by lateral competition between the strong, persistent central fixation peak and the relatively weak peripheral cue input. This appears to contrast with previous behavioral and neurophysiological work that suggests the visual competition in overlap conditions requires additional input from cortical mechanisms, including frontal eye fields and the dorsolateral prefrontal cortex (Fan et al., 2005; Johnson & De Haan, 2015; Johnson et al., 1991). One possibility is that the dynamics captured by the gaze change node reflect these frontal inputs, biasing attention away from the central stimulus. Recently, Buss et al. (2021) proposed methods to map neural activity in dynamic field models to hemodynamic responses measured using fMRI or fNIRS; such methods could be used to directly investigate links between the DF model and infant brain activity.

## 7 | CONCLUSION

In  this  study,  we/uni00A0 tested/uni00A0 five/uni00A0 model  predictions/uni00A0 regarding  early/uni00A0 orienting  toward  peripherally located stimuli/uni00A0in/uni00A0visually competitive and non- competitive/uni00A0contexts, testing a cohort of 5- , 7- , and 10- month- old infants./uni00A0Infants' looking during these tasks revealed/uni00A0slowed shifting/uni00A0toward peripheral stimuli with/uni00A0added/uni00A0 competition./uni00A0 Visual  competition also increased the accuracy of shifts when invalid cues were presented, particularly for 7- month- old infants, suggesting previously overlooked adaptive benefits./uni00A0The presence of early peripheral cues affected later visual shifts toward target stimuli with differing patterns when competition was present versus when it was absent./uni00A0Model simulations suggested that age differences in observed competition effects were largely driven by stronger neural interactions within cortical fields. The same developmental mechanisms that had captured impacts of infants' covert orienting within non- competitive contexts extended to infants' orienting within competitive contexts.

## ACKNOWLEDGMENTS

|

<!-- image -->

<!-- image -->

We would like to thank the research assistants and participating families who made this work possible. Funding for this study was provided by R01HD083287 awarded to J. Spencer. The authors declare no conflicts of interest with regard to the funding source for this study.

## ORCID

John P. Spencer /uni00A0 https://orcid.org/0000-0002-7320-144X Shannon Ross- Sheehy /uni00A0 https://orcid.org/0000-0001-7799-8524 Bret Eschman /uni00A0 https://orcid.org/0000-0001-9379-154X

## REFERENCES

Amso, D., & Scerif, G. (2015). The attentive brain: Insights from developmental cognitive neuroscience. Nature Reviews Neuroscience , 16 (10), 606- 619. https://doi.org/10.1038/nrn4025

Brune, C. W., & Woodward, A. L. (2007). Social cognition and social responsiveness in 10- month- old infants. Journal of Cognition and Development , 8 (2), 133- 158. https://doi.org/10.1080/15248 37070 1202331

Buss, A. T., Magnotta, V., Penny, W., Schöner, G., Huppert, T., & Spencer, J. P. (2021). How do neural processes give rise to cognition? Simultaneously predicting brain and behavior with a dynamic model of visual working memory. Psychological Review , 128 (2), 362- 395. https://doi.org/10.1037/rev00 00264

Butcher, P. R., Kalverboer, A. F., & Geuze, R. H. (2000). Infants' shifts of gaze from a central to a peripheral stimulus: A longitudinal study of development between 6 and 26 weeks. Infant Behavior and Development , 23 (1), 3- 21. https://doi.org/10.1016/S0163 - 6383(00)00031 - X

Cao, M., Huang, H., & He, Y. (2017). Developmental connectomics from infancy through early childhood. Trends in Neurosciences , 40 (8), 494- 506. https://doi.org/10.1016/j.tins.2017.06.003

Colombo, J. (2001). The development of visual attention in infancy. Annual Review of Psychology , 52 (1), 337- 367. https://doi.org/10.1146/annur ev.psych.52.1.337

Corbetta, M., Kincade, J. M., & Shulman, G. L. (2002). Neural systems for visual orienting and their relationships to spatial working memory. Journal of Cognitive Neuroscience , 14 (3), 508- 523. https://doi.org/10.1162/08989 29023 17362029

Cousijn, J., Hessels, R. S., Van der Stigchel, S., & Kemner, C. (2017). Evaluation of the psychometric properties of the gap- overlap task in 10- Month- Old Infants. Infancy , 22 (4), 571- 579. https://doi.org/10.1111/infa.12185

Cuevas, K., & Bell, M. A. (2011). EEG and ECG from 5 to 10 months of age: Developmental changes in baseline activation and cognitive processing during a working memory task. International Journal of Psychophysiology , 80 (2), 119- 128. https://doi.org/10.1016/j.ijpsy cho.2011.02.009

Fan, J., McCandliss, B. D., Fossella, J., Flombaum, J. I., & Posner, M. I. (2005). The activation of attention networks. NeuroImage , 26 (2), 471- 479. https://doi.org/10.1016/j.neuro image.2005.02.004

Frick, J. E., Colombo, J., & Saxon, T. F. (1999). Individual and developmental differences in disengagement of fixation in early infancy. Child Development , 70 (3), 537- 548. https://doi.org/10.1111/1467- 8624.00039

Hood, B. M., & Atkinson, J. (1993). Disengaging visual attention in the infant and adult. Infant Behavior and Development , 16 (4), 405- 422. https://doi.org/10.1016/0163- 6383(93)80001 - O

Huestegge, L., & Koch, I. (2010). Fixation disengagement enhances peripheral perceptual processing: Evidence for  a  perceptual  gap  effect. Experimental  Brain  Research , 201 (4),  631- 640.  https://doi.org/10.1007/s0022 1- 009- 2080- 2

Johnson, M. H., & de Haan, M. (2015). Developmental cognitive neuroscience (4th ed.). Blackwell Publishers Ltd. Johnson,  M.  H.,  Posner,  M.  I.,  &  Rothbart,  M.  K.  (1991).  Components  of  visual  orienting  in  early  infancy: Contingency learning, anticipatory looking, and disengaging. Journal of Cognitive Neuroscience , 3 (4), 335344. https://doi.org/10.1162/jocn.1991.3.4.335

Katyal, S., Zughni, S., Greene, C., & Ress, D. (2010). Topography of covert visual attention in human superior colliculus. Journal of Neurophysiology , 104 (6), 3074- 3083. https://doi.org/10.1152/jn.00283.2010

Krauzlis, R. J., Lovejoy, L. P., & Zénon, A. (2013). Superior colliculus and visual spatial attention. Annual Review of Neuroscience , 36 , 165- 182. https://doi.org/10.1146/annur ev- neuro - 06201 2- 170249

|

<!-- image -->

Kulke, L., Atkinson, J., & Braddick, O. (2015). Automatic detection of attention shifts in infancy: Eye tracking in the fixation shift paradigm. PLoS One , 10 (12), e0142505. https://doi.org/10.1371/journ al.pone.0142505

Kulke, L. V., Atkinson, J., & Braddick, O. (2016). Neural differences between covert and overt attention studied using EEG with simultaneous remote eye tracking. Frontiers in Human Neuroscience , 10 (592), 1- 11. https:// doi.org/10.3389/fnhum.2016.00592

Kulke, L., Atkinson, J., & Braddick, O. (2017). Neural mechanisms of attention become more specialised during infancy: Insights from combined eye tracking and EEG. Developmental Psychobiology , 59 (2), 250- 260. https:// doi.org/10.1002/dev.21494

Kulke, L., Atkinson, J., & Braddick, O. (2020). Relation between event- related potential latency and saccade latency in overt shifts of attention. Perception , 49 (4), 468- 483. https://doi.org/10.1177/03010 06620 911869

Matsuzawa, M., & Shimojo, S. (1997). Infants' fast saccades in the gap paradigm and development of visual attention. Infant Behavior and Development , 20 (4), 449- 455. https://doi.org/10.1016/S0163 - 6383(97)90035 - 7

Perone, S., Simmering, V. R., & Spencer, J. P. (2011). Stronger neural dynamics capture changes in infants' visual  working  memory  capacity  over  development. Developmental  Science , 14 (6),  1379- 1392.  https://doi. org/10.1111/j.1467- 7687.2011.01083.x

Petersen, S. E., & Posner, M. I. (2012). The attention system of the human brain: 20 years after. Annual Review of Neuroscience , 35 , 73- 89. https://doi.org/10.1146/annur ev- neuro - 06211 1- 150525

Posner, M. I., & Petersen, S. E. (1990). The attention system of the human brain. Annual Review of Neuroscience , 13 (1), 25- 42. https://doi.org/10.1146/annur ev.ne.13.030190.000325

Richards, J. E. (2000). Localizing the development of covert attention in infants with scalp event- related potentials. Developmental Psychology , 36 (1), 91- 108. https://doi.org/10.1037/001649.36.1.91

Richards, J. E. (2001). Cortical indexes of saccade planning following covert orienting in 20- week- old infants. Infancy , 2 (2), 135- 157. https://doi.org/10.1207/S1532 7078I N0202\_2

Richards,  J.  E.  (2005).  Localizing  cortical  sources  of  event- related  potentials  in  infants'  covert  orienting. Developmental Science , 8 (3), 255- 278. https://doi.org/10.1111/j.1467- 7687.2005.00414.x

Ross- Sheehy,  S.,  Perone,  S.,  Macek,  K.  L.,  &  Eschman,  B.  (2017). Visual  orienting  and  attention  deficits  in  5and 10- month- old preterm infants. Infant Behavior and Development , 46 ,  80- 90.  https://doi.org/10.1016/j. infbeh.2016.12.004

Ross- Sheehy, S., Reynolds, E., & Eschman, B. (2020). Evidence for attentional phenotypes in infancy and their role in visual cognitive performance. Brain Sciences , 10 (9), 605. https://doi.org/10.3390/brain sci10 090605

Ross- Sheehy, S., Schneegans, S., & Spencer, J. P. (2015). The infant orienting with attention task: Assessing the neural basis of spatial attention in infancy. Infancy , 20 (5), 467- 506. https://doi.org/10.1111/infa.12087

Saez de Urabain, I. R., Nuthmann, A., Johnson, M. H., & Smith, T. J. (2017). Disentangling the mechanisms underlying infant fixation durations in scene perception: A computational account. Vision Research , 134 , 43- 59. https://doi.org/10.1016/j.visres.2016.10.015

Samuelson, L. K., Smith, L. B., Perry, L. K., & Spencer, J. P. (2011). Grounding word learning in space. PLoS One , 6 (12), e28095. https://doi.org/10.1371/journ al.pone.0028095

Schöner, G., Spencer, J. P., & the DFT Research Group (2016). Dynamic thinking: A primer on dynamic field theory . Oxford University Press.

Schutte, A. R., & Spencer, J. P. (2009). Tests of the dynamic field theory and the spatial precision hypothesis: Capturing  a  qualitative  developmental  transition  in  spatial  working  memory. Journal  of  Experimental Psychology: Human Perception and Performance , 35 (6), 1698- 1725. https://doi.org/10.1037/a0015794

Schutte, A. R., Spencer, J. P., & Schöner, G. (2003). Testing the dynamic field theory: Working memory for locations becomes more spatially precise over development. Child Development , 74 (5), 1393- 1417. https://doi. org/10.1111/1467- 8624.00614

Spencer, J. P., Simmering, V. R., Schutte, A. R., & Schöner, G. (2007). What does theoretical neuroscience have to offer the study of behavioral development? Insights from a dynamic field theory of spatial cognition. In J. M. Plumert, & J. P. Spencer (Eds.), The emerging spatial mind (pp. 320- 361). Oxford University Press. https://doi. org/10.1093/acpro f:oso/97801 95189 223.003.0014

Wentworth,  N.,  &  Haith,  M.  M.  (1998).  Infants'  acquisition  of  spatiotemporal  expectations. Developmental Psychology , 34 (2), 247- 257. https://doi.org/10.1037/0012- 1649.34.2.247

Xie, W., & Richards, J. E. (2017). The relation between infant covert orienting, sustained attention and brain activity. Brain Topography , 30 (2), 198- 219. https://doi.org/10.1007/s1054 8- 016- 0505- 3

|

<!-- image -->

<!-- image -->

Yuan, L., Uttal, D., & Franconeri, S. (2016). Are categorical spatial relations encoded by shifting visual attention between objects? PLoS One , 11 (10), e0163141. https://doi.org/10.1371/journ al.pone.0163141

How to cite this article: Spencer, J. P., Ross- Sheehy, S., & Eschman, B. (2022). Testing predictions of a neural process model of visual attention in infancy across competitive and non- competitive contexts. Infancy , 27, 389- 411. https://doi.org/10.1111/infa.12457