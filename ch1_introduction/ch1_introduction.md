# Chapter 1: Introduction

---

# **1.1   What is AI**

- Pensées vs comportements
- Modélisation d’humains vs atteindre le meilleur résultat

## **Acting humanly: Turing test**

- Il est au final plus important de comprendre les principes sous tenants à l’intelligence (allégorie du vol où on a arrêté de copier les oiseaux)

## **Thinking humanly: Cognitive modeling approach**

- *cognitive science*
    - mix entre les modèles informatiques originaires de l’IA et des techniques expérimentales originaires de la psychologie

## **Thinking rationally: The “laws of thought” approach**

- Besoin d’une théorie de l’action rationnelle pour générer un comportement intelligent

## **Acting rationally: The rational agent approach**

- Laws of thoughts: faire des déductions correctes
- Agir rationnellement :
    - knowledge representation
    - reasoning
    - ⇒ bonnes décisions
- *Rational-agent approach* vs *laws of thoughts*:
    - plus général (faire de bonnes déductions n’est qu’une façon d’être rationnel)
    - plus simple à développer scientifiquement

<aside>
💡 **Standard model of AI**: *AI has focused on the study and construction of agents that do the right thing.*

</aside>

- Dans un monde complexe, c’est impossible de toujours prendre la meilleure décision (*limited rationality*)

## **Beneficial machines**

- *Standard model*: Pas idéal car on ne peut/veut pas toujours donner un objectif parfaitement défini à une machine
    - difficile à faire dans le vrai monde
- *Value alignment problem*: Arriver à faire correspondre nos vraies préférences à un objectif programmable
- On souhaite que les machines soient *provably beneficial* aux humains

# **1.2   The Foundations of Artificial Intelligence**

## **Philosophy**

- Les connaissances sont la base de l’action, et sont enregistrées dans une forme de langage interne qui permet de choisir une action adaptée

## **Mathematics**

- Logique formelle → [logique de premier ordre](https://en.wikipedia.org/wiki/First-order_logic)
- Généraliser la logique aux situations d’information incertaine → Théorie des probabilités
- Ajout de la mathématisation de la [*computation*](https://en.wikipedia.org/wiki/Computation) à la logique et aux probabilités
- [Théorème de l’incomplétude](https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems) (Gödel, XXème)
    - Des limites à la déduction existent
    - Certaines fonctions ne peuvent pas être représentées par un algorithme et donc ne peuvent pas être calculées
- Intractabilité:
    - Le temps requit par un problème intractable grandit exponentiellement avec la taille (nombre) des instances

## **Economics**

- Maximum expected value (Arnauld, 1662)
- Maximisation de l’utilité attendue (Bernoulli, 1738)
- Decision theory:
    - Combiner les probabilités et l’utilité pour créer un modèle complet et formel de la prise de décision individuelle
- Satisfaction (Simon, 1978 Nobel prize):
    - Prendre des décisions qui sont satisfaisantes et pas optimales

## **Neuroscience**

- Les fonctions cognitives sont le résultat d’opérations électrochimiques

<aside>
🧠 *A collection of simple cells can lead to thought, action, and consciousness*
or
*Brains cause minds*

</aside>

- Machines et cerveaux ont des fonctionnements et des performances différentes
    - Singularité: Les ordinateurs atteindront un niveau surhumain

## **Psychology**

- Psychologie cognitive (James, XIX-XXème)
- Humains et animaux peuvent être qualifiés de *information-processing machines*

## **Computer engineering**

- Création d’*hardware* et de *software* de plus en plus puissants
    - Création récente d’ordinateurs spécifiques pour l’AI
    - Informatique quantique
    - Améliorations logicielles

## **Control theory and cybernetics**

- Développement de la *control theory* (Wiener, XXème)
    - Mécanisme de régulation grâce à la minimisation de l’erreur
- Appareils homéostatiques (1940-52):
    - Utilisation de boucles de rétroaction
- *Stochastic optimal control*:
    - Maximiser (*ndlr*: minimiser?) une fonction de coût en fonction du temps

## **Linguistics**

- *Computational linguistics* ou *natural langage processing*
    - Compréhension du sujet et du contexte, pas de la structure des phrases
- Lien entre *knowledge representation* et linguistique

# **1.3   The History of Artificial Intelligence**

- Histoire longue et complexe, avec beaucoup de hauts (espoirs délirants, investissements, succès) et de bas
- Successions d’améliorations de technologies existantes et de nouvelles innovations

# **1.4   The state of the art**

- L’IA s’est beaucoup améliorée avec le temps, en méthodologie et en théorie
- Logique booléenne ➡️ raisonnement probabilistique
- Connaissances “hardcodées” ➡️ machine learning basé sur les données

⇒ Amélioration des performances des systèmes et applications à d’autres domaines

# **1.5   Risks and benefits of AI**

- Plus les domaines d’application sont larges, plus les risques et conséquences éthiques sont larges
- Apparition potentielle d’une IA superintelligence et difficile à contrôler
    - Modification de notre façon de concevoir l’IA

# 1.A   Exercises

1. Define in your own words: (a) intelligence, (b) artificial intelligence, (c) agent, (d) rationality, (e) logical reasoning.
    1. Intelligence is the capacity to creatively solve problems
    2. AI is a field of research that aims at creating programs (agents) that can navigate their environment, make decisions, and perform actions by themselves
    3. An agent is a sum of programs encapsulated in a single entity that enables it to sense and respond to its environment
    4. Rationality is the capacity to take the best possible decision in a given (potentially uncertain) context
    5. Logical reasoning is the capacity to respond to a stimulus or take a decision based on reproducible laws (not right, its more about creating new facts derived from proved older facts that are logically proved as well)
2. Read Turing’s original paper on AI [Turing:1950](https://aimacode.github.io/aima-exercises/intro-exercises/). In the paper, he discusses several objections to his proposed enterprise and his test for intelligence. Which objections still carry weight? Are his refutations valid? Can you think of new objections arising from developments since he wrote the paper? In the paper, he predicts that, by the year 2000, a computer will have a 30% chance of passing a five-minute Turing Test with an unskilled interrogator. What chance do you think a computer would have today? In another 50 years?
    1. Objection 1: Theological — I don’t think the value of this argument has changed in 74 years. I am far from versed in theology, but I don’t believe in immortal souls etc. I also don’t see what are the arguments to state that humans have souls but not animals, *esp* taking into account more eastern view on spirituality. Would a mechanical body be less adequate to host a soul than a fleshy one? Maybe, maybe not, who knows. My main issue with this objection is that it is based on beliefs, which don’t provide a solid basis for logical arguments.
    2. Objection 2: Head in the sand — This argument has been used a lot regarding the debates around the consciousness of LLMs (mainly between 2022 and 2023). While I don’t think LLMs are close to consciousness in any way, shape or form, I also find that many commentators completely refuted the idea of artificial super-intelligence on the basis of a felt human superiority. I can understand that this refutal could have been used to focus on current AI issues instead of debates around robots’ rights. However, I don’t think it is a legitimate refutal either.
    3. Objection 3: Mathematical — I am not perfectly sure Gödel’s theorem applies perfectly to the Imitation Game. Machine learning approaches have delivered solid results especially in the domain of NLP. While scalability of LLMs to other task or to reasoning (or even the ability of bigger model to solve their current issues such as hallucinations) is an active area of research, I don’t think it’s linked. I also believe that humans can indeed be wrong, so machines being wrong is not an objection to machine intelligence in my opinion.
    4. Objection 4: the Argument from Consciousness — The hardest to decide on so far, but also the most discussed today. The *viva voce* is a very interesting approach to keep the Imitation Game relevant. However, LLMs have been showed to be able to explain poetry and emotions simply based on their training data. A difference between LLMs and a parrot-fashion learned poem is the capacity of a human to actually reason over the arguments offered during the discussion, while LLMs would probably simply repeat the same things in a loop.
    5. Objection 5: Various Disabilities — The list of things AI can’t do has moved around a lot in the last decades. I think it is both a reflection of our refusal to ever acknowledge a machine as our equal, and of our better understanding of what makes human intelligence what it is. In that sense, AI is a fantastic tool to understand ourselves (mostly our brains) better. 
        1. Interesting thought about machine that would fix their own code (does adjusting weights count?). The fact machines don’t make mistakes is also quite not right anymore with DL. 
    6. Objection 6: Lady Lovelace’s — The inability to learn or create anything new is also vividly discussed currently. is AI-generated art new? Is art by a debuting artist taking heavy inspiration from masters’ work new? I would consider them different forms of art. I would also say that features detected and used by e.g. CV models, or strategies used by AlphaGo are definitely new and different from what humans do.
    7. Objection 7: Continuity in the Nervous System — Probabilities indeed some form of continuity in machines, eg activation functions in NN. I also don’t believe machine intelligence will necessarily come from respecting every law governing the human brain (planes don’t flap their wings…).
    8. Objectif 8: Informality of Behavior — Indeed, events not taken into account during training still are one of the biggest problems in AI/ML (self-driving cars and unplanned circumstances, LLMs can’t use tokens that don’t exist in their training corpus, etc). 
    9. Objection 9: Extra-Sensory Perception — 🤨
    10. I believe that today, most humans (that speak a language “known” by LLMs) could be fooled by large language models. The examples are numerous, from Blake Lemoine to Replika users. I have no idea how to estimate the numbers however and have no idea how such feat is done.
3. Every year the Loebner Prize is awarded to the program that comes closest to passing a version of the [Turing Test](https://en.wikipedia.org/wiki/Turing_test). Research and report on the latest winner of the Loebner prize. What techniques does it use? How does it advance the state of the art in AI?
    1. Seems like it hasn’t happened since 2019. It also focused heavily on chatbots in the last editions, which makes sense considering what was discussed above regarding LLMs and Turing’s test. It seems to me that (like for Asimov), the impact that the Internet would have on us was almost impossible to predict in the early second part of the XXth century. Indeed, LLMs didn’t really master human language and emotions (or, as Turing wrote, mastered English as a reasoning machine). Instead, the simply absurd amount of training data (publicly) available there and the huge advances in computing power enabled us to cheat the Turing test, making it way less obvious as an adequate test for intelligence today. I don’t know what the equivalent would be today, but that seems interesting to research. Google → “What is the new best test for artificial intelligence?”
4. Are reflex actions (such as flinching from a hot stove) rational? Are they intelligent?
    1. They are rational because thinking and reflecting would be inadequate and lead to a undesirable outcome. They is intelligent if we define intelligence as acting rationally. It isn’t if we define intelligence as knowledge and reasoning based.
5. There are well-known classes of problems that are intractably difficult for computers, and other classes that are provably undecidable. Does this mean that AI is impossible?
    1. No. I would say that agents with the capacity to be unsure can be defined as intelligent. Indeed, if we take into account to fact that AI always compared to human intelligence, we can see that some problems are unsolvable for some people. That doesn’t mean they are not intelligent. 
6. Suppose we extend Evans’s *SYSTEM* program so that it can score 200 on a standard IQ test. Would we then have a program more intelligent than a human? Explain.
    1. I suppose that this is the system we are talking about? Quote from the manual: “Tom Evans’s ANALOGY program (1968) solved geometric analogy problems that appear in IQ tests.”
    2. I would say not simply for the fact that I don’t recognize IQ as a correct assessment of human intelligence (It is linked to multiple issues and wrong measurements). Also, very much like a program, a human could prepare for these exercises to score higher (an AI could be trained specifically for the test and not do good in any other measure of intelligence). 
7. The neural structure of the sea slug *Aplysis* has been widely studied (first by Nobel Laureate Eric Kandel) because it has only about 20,000 neurons, most of them large and easily manipulated. Assuming that the cycle time for an *Aplysis* neuron is roughly the same as for a human neuron, how does the computational power, in terms of memory updates per second, compare with the high-end computer described in (Figure [1.3](https://aimacode.github.io/aima-exercises/figures/computer-brain-table.png))?
8. How could introspection—reporting on one’s inner thoughts—be inaccurate? Could I be wrong about what I’m thinking? Discuss.
    1. Not inaccurate but more incomplete, and that incompleteness can lead to inaccurate conclusions. 
9. To what extent are the following computer systems instances of artificial intelligence:
- Supermarket bar code scanners.
- Web search engines.
- Voice-activated telephone menus.
- Internet routing algorithms that respond dynamically to the state of the network.
    1. Computer vision is a well known field of AI. It is an instance of AI in the sense that it is replicating something we humans use to interact with our environment and take appropriate actions in response to it. The fact that the code is linked to a specific item is not intelligence (afaik) but simple correspondance using a mapping system and codes.
    2. The systems are examples of recommender systems. They are able to use your search data (previous inputs) to provide results more fitting to your preferences (at least this is the sales pitch). In this case, the system uses clustering to recommend results that people with the same preferences happened to find fitting. A lot more can be described as using intelligence as well, for example the spelling errors recognition.
    3. Speech recognition is comparable to computer vision because it is also emulating a human sense. In this case, the system is able to link what you are outputting and link it to a predefined item in a menu.
    4. Not sure about this one. Finding the best route in a changing environment shows adaptability.
10. /
11. Many of the computational models of cognitive activities that have been proposed involve quite complex mathematical operations, such as convolving an image with a Gaussian or finding a minimum of the entropy function. Most humans (and certainly all animals) never learn this kind of mathematics at all, almost no one learns it before college, and almost no one can compute the convolution of a function with a Gaussian in their head. What sense does it make to say that the “vision system” is doing this kind of mathematics, whereas the actual person has no idea how to do it?
    1. We do a whole lot of things without knowing/understanding how it works. I’m pretty sure no one can map the entire neural influxes needed to have any thought whatsoever. Some things happen following mathematical rules that cannot be understood by the majority of humans, even less so computed.
12. Some authors have claimed that perception and motor skills are the most important part of intelligence, and that “higher level” capacities are necessarily parasitic—simple add-ons to these underlying facilities. Certainly, most of evolution and a large part of the brain have been devoted to perception and motor skills, whereas AI has found tasks such as game playing and logical inference to be easier, in many ways, than perceiving and acting in the real world. Do you think that AI’s traditional focus on higher-level cognitive abilities is misplaced?
    1. I wouldn’t say it’s misplaced. Motor skills for example are difficult to test in the real world because of the faster evolution of software compared to hardware. It’s also notoriously difficult to adapt AI to the real world because of the many, many edge cases present. Autonomous cars are a good example of that. We often try to have agents that can perform well in any environment, where animals and humans are traditionally adapted to a specific one. Also, the focus on games comes from this idea of an ideal world in which the rules are clear and unchanged. The traditional direction from games to simulations to the real world makes sense in that way. 
13. Why would evolution tend to result in systems that act rationally? What goals are such systems designed to achieve?
    1. Because evolution selects the most fitted individuals (agents?) in a given environment. Being rational is simply maximizing the performance, so is aligned with this idea. 
14. Is AI a science, or is it engineering? Or neither or both? Explain.
    1. AI is a field of science that is coming from and influenced by a lot of other domains, among which engineering. To build on the LLM example, the text embeddings and vectorial representations take a lot from linguistics, where improvements in computation power comes from engineering.
15. “Surely computers cannot be intelligent—they can do only what their programmers tell them.” Is the latter statement true, and does it imply the former?
    1. It is, in a sense, true. While AI programmers don’t explicitly code the different aspects of the agents, they define their utility functions and performance measure. However, agents can, and often do, act in creative and novel ways to follow these rules in a way that the programmers didn’t anticipate.
16. “Surely animals cannot be intelligent—they can do only what their genes tell them.” Is the latter statement true, and does it imply the former?
    1. I would say that in this case, because the mechanism is different in my opinion, it is untrue. Genes are what enable intelligent behavior to arise. Where this distinction comes from is more difficult to know for me, but I think it has to do with the fact that the intelligence animals display is not coming from humans maybe. Also, genes don’t give you all the information you need, you learn with experience and experiments in the real world. Something AI cannot do (yet).  
17. “Surely animals, humans, and computers cannot be intelligent—they can do only what their constituent atoms are told to do by the laws of physics.” Is the latter statement true, and does it imply the former?
    1. Same argument than above but stronger; laws of physics are not much help when deciding what food to order (tbh that doesn’t sound like a good punchline, not even a good argument…).
18. Examine the AI literature to discover whether the following tasks can currently be solved by computers: - Playing a decent game of table tennis (Ping-Pong). - Driving in the center of Cairo, Egypt. - Driving in Victorville, California. - Buying a week’s worth of groceries at the market. - Buying a week’s worth of groceries on the Web. - Playing a decent game of bridge at a competitive level. - Discovering and proving new mathematical theorems. - Writing an intentionally funny story. - Giving competent legal advice in a specialized area of law. - Translating spoken English into spoken Swedish in real time. - Performing a complex surgical operation.
    1. https://spectrum.ieee.org/robots-playing-ping-pong-whats-real-and-whats-not
    2. https://waymo.com/ — It’s possible in SF, should be in Cairo given sufficient training data (though I must admit I don’t know how the traffic is there). Should be easier in California.
    3. In the market no, no robot functions at that level of real-world interaction yet.
    4. LLM agent should be able to do it if we believe the AI gurus (see Rabbit R1). It should be easy to do if the grocery list and supermarket are determined in advance, and if the supermarket has a good API.
    5. [https://www.quora.com/Can-AI-play-perfect-Bridge#:~:text=Yes%2C computer bridge programs play,plays%2C but it's all inferential](https://www.quora.com/Can-AI-play-perfect-Bridge#:~:text=Yes%2C%20computer%20bridge%20programs%20play,plays%2C%20but%20it's%20all%20inferential)
    6. [https://en.wikipedia.org/wiki/Automated_theorem_proving#:~:text=Interactive provers are used for,time%2C namely the Robbins conjecture](https://en.wikipedia.org/wiki/Automated_theorem_proving#:~:text=Interactive%20provers%20are%20used%20for,time%2C%20namely%20the%20Robbins%20conjecture).
    7. Yes (or no, depending on the definition of intentionality).
    8. Yes (if you don’t take into account hallucinations).
    9. Yes.
    10. https://www.cureus.com/articles/204683-future-of-artificial-intelligence-in-surgery-a-narrative-review#!/
19. For the currently infeasible tasks, try to find out what the difficulties are and predict when, if ever, they will be overcome.
    1. A lot of issues have to do with hardware limitations (real world interactions) or lack of data. I believe they could be solved in the next 5 to 10 years.
20. Various subfields of AI have held contests by defining a standard task and inviting researchers to do their best. Examples include the DARPA Grand Challenge for robotic cars, the International Planning Competition, the Robocup robotic soccer league, the TREC information retrieval event, and contests in machine translation and speech recognition. Investigate five of these contests and describe the progress made over the years. To what degree have the contests advanced the state of the art in AI? To what degree do they hurt the field by drawing energy away from new ideas?
    1. https://en.wikipedia.org/wiki/DARPA_Grand_Challenge
    2. https://www.icaps-conference.org/competitions/
    3. https://www.robocup.org/leagues/18
    4. https://trec.nist.gov/
    5. https://www.nist.gov/programs-projects/machine-translation