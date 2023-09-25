from fpdf import FPDF


class PDF(FPDF):

    def doc_title(self, label):
        self.set_font("helvetica", "B", 16)  # Aqui definimos "B" para negrito
        self.cell(0, 10, label, "L")
        self.ln(15)
        

    def doc_text(self, text):
        self.set_font("helvetica", "", 12)  # Aqui definimos "" para fonte normal (não negrito)
        self.multi_cell(0, 7, text)
        self.ln()

    def doc_image(self, img, x, y, w, h):
        self.image(img, x, y, w, h)





\



pdf = PDF()

pdf.add_page()

pdf.set_y(30)  # Ajuste essa posição conforme necessário
pdf.set_font("Arial",size=14)
pdf.cell(0,50, "RELATÓRIO KICK", align="C", ln=True)
# Defina a posição vertical para o título
pdf.set_y(57)  # Ajuste essa posição conforme necessário
pdf.set_font("Arial",size=21)
pdf.cell(0,50, "DESIGUALDADE EDUCACIONAL BRASILEIRA", align="C", ln=True)

pdf.set_font("Arial", size=12)
pdf.cell(0, 10, txt="Desenvolvido por Gabriela Orlandin Lopes", ln=True, align="C")

pdf.set_font("Arial", size=12)
pdf.cell(0,15, "Ribeirão Preto, 2023.", ln=True, align="C")


pdf.add_page()

pdf.doc_title("RELATÓRIO - DESIGUALDADE EDUCACIONAL NO BRASIL")


pdf.doc_text(" A desigualdade educacional no Brasil é um desafio complexo e multifacetado que tem implicações profundas no desenvolvimento do país. Em um cenário global, onde a educação desempenha um papel fundamental na ascensão econômica e social das nações, o Brasil ainda luta para oferecer um sistema público de ensino eficaz e igualitário. Esta disparidade entre o potencial do país, classificado como a 12ª maior economia do mundo, e a realidade de seu sistema educacional é evidente em nossa trajetória de crescimento.")

pdf.doc_text("Este relatório tem como missão investigar com profundidade a problemática da desigualdade educacional no Brasil. Com base em um amplo conjunto de dados relacionados à educação no país, apresentamos uma série de análises de dados disponibilizados através de sites governamentais, que abrangem uma variedade de áreas. Estas análises vão desde a distribuição de cursos por categoria administrativa até uma cuidadosa comparação das médias de mestrado e doutorado, explorando diferentes regiões e anos de avaliação. O objetivo é oferecer uma visão abrangente e embasada sobre as disparidades educacionais em território brasileiro, contribuindo para uma compreensão mais profunda dessa questão crítica.")

pdf.ln(10)
pdf.doc_text('1.Informações orgaizadas somente por nome da instituição, curso e grau. \nIniciamos a partir da seleção das informações da tabela focada nas colunas "NOME_IES," "NOME_CURSO" e "GRAU". Podemos iniciar uma análise mais detalhada para entender melhor o panorama educacional no Brasil.\nDiversidade de Instituições de Ensino: Existem várias instituições de ensino representadas na tabela (NOME_IES), o que indica uma diversidade de opções para os estudantes.\nVariedade de Cursos: A coluna "NOME_CURSO" mostra uma variedade de cursos oferecidos por essas instituições. Isso reflete a amplitude das opções de cursos disponíveis para os estudantes, abrangendo diferentes áreas de conhecimento.\nDiferentes Níveis de Grau: A coluna "GRAU" revela os diferentes níveis de grau educacional oferecidos pelas instituições, como graduação, pós-graduação, mestrado, doutorado, entre outros. Isso demonstra a diversidade de oportunidades educacionais em termos de níveis de ensino.\n\nA presença de várias instituições, cursos e níveis de grau oferece aos estudantes a oportunidade de escolher programas educacionais que atendam às suas necessidades e interesses específicos. Por outro lado, a diversidade de opções também pode tornar a tomada de decisão mais complexa para os estudantes, que precisam considerar vários fatores ao escolher uma instituição, um curso e um nível de grau. Em resumo, a análise das colunas "NOME_IES," "NOME_CURSO," e "GRAU" destaca a diversidade e complexidade do cenário educacional no Brasil, fornecendo aos estudantes uma variedade de opções, mas também, demandando que as decisões educacionais sejam cuidadosamente avaliadas e embasadas em informações sólidas. Dada a ampla gama de escolhas, é importante que os estudantes recebam orientação educacional adequada para tomar decisões informadas sobre sua trajetória acadêmica.')
pdf.ln(10)

pdf.doc_text("2. Analisa a quantidade de cursos oferecidos pela categoria admistrativa de cada instituição de ensino. \nFoi realizado uma breve análise da contagem de cursos por categoria administrativa em instituições de ensino no Brasil e obtivemos os seguintes resultados: \nPrivada com fins lucrativos: Há uma predominância significativa de instituições de ensino privadas com fins lucrativos, com um total de 761.454 cursos. \nPrivada sem fins lucrativos: As instituições de ensino privadas sem fins lucrativos também apresentam uma representação considerável, com um total de 112.023 cursos. \nPública Federal: As instituições de ensino públicas federais oferecem um número considerável de cursos, totalizando 14.802. \nPública Estadual: As instituições de ensino públicas estaduais oferecem um total de 9.980 cursos, o que é significativo, embora menor em comparação com as categorias privadas. Pública Municipal: As instituições de ensino públicas municipais oferecem um total de 3.634 cursos. \nEspecial: A categoria \"Especial\" representa um número menor de cursos, com um total de 783. Essa distribuição de cursos por categoria administrativa é importante para compreender a diversidade de opções educacionais disponíveis no Brasil. \n\nA predominância das instituições privadas com fins lucrativos indica a presença de um mercado educacional robusto, enquanto as instituições públicas desempenham um papel fundamental no acesso à educação de qualidade. Esses dados fornecem insights valiosos para formuladores de políticas educacionais e instituições de ensino, auxiliando na tomada de decisões informadas sobre alocação de recursos, expansão de cursos e estratégias para promover a equidade no acesso à educação.")

pdf.ln(10)

pdf.doc_text("3. Apresenta uma análise da quantidade de instituições de ensino por região no Brasil. \nSudeste: A região Sudeste do Brasil possui o maior número de instituições de ensino, com um total de 1.469. Isso é consistente com o fato de que essa região é a mais populosa e economicamente desenvolvida do país. \nNordeste: A região Nordeste é a segunda em termos de quantidade de instituições, com 853. Isso reflete a importância da educação nessa parte do Brasil, que abriga uma população significativa. \
\nSul: A região Sul possui um total de 1.028 instituições de ensino, indicando uma presença considerável de instituições educacionais. \
\nCentro-Oeste: A região Centro-Oeste, embora menos populosa que as regiões anteriores, ainda conta com 723 instituições de ensino. \
\nNorte: A região Norte possui 598 instituições de ensino, demonstrando que também contribui significativamente para a oferta educacional no país. \
\nIgnorado/Exterior: A categoria \"Ignorado/Exterior\" contém 191 instituições, que podem ser instituições não especificadas geograficamente ou localizadas no exterior. \
\n\nA análise da quantidade de instituições de ensino por região no Brasil revela um panorama diversificado e dinâmico da infraestrutura educacional do país. Cada região contribui de forma única para a oferta de oportunidades educacionais, refletindo suas peculiaridades demográficas, econômicas e geográficas. Essa distribuição de instituições de ensino desempenha um papel crucial na discussão sobre desigualdade educacional no Brasil. \
A desigualdade educacional está intrinsecamente relacionada a fatores como acesso limitado à educação de qualidade, disparidades na distribuição de recursos educacionais e desequilíbrios econômicos regionais. Nesse contexto, a análise da quantidade de instituições de ensino por região oferece insights valiosos. \
A região Sudeste, a mais populosa e economicamente desenvolvida do Brasil, concentra o maior número de instituições de ensino. Embora isso seja um reflexo de sua importância socioeconômica, também destaca uma tendência preocupante de centralização educacional. Muitos brasileiros de outras regiões podem enfrentar desafios adicionais para acessar instituições de ensino de alta qualidade, especialmente se considerarmos as barreiras geográficas e econômicas.\nA seguir, a representação visual dessa análise por meio de um gráfico de barras:")

pdf.doc_image("grafico_quantidade_cursos_por_regiao.png", 25, 185, 150, 100)  # Ajuste a coordenada Y para 250
pdf.ln(85)

pdf.doc_text('''
4. Verificando quantidade de cursos oferecidos por Instituição e total de Instituições:\n\nDisparidade na Quantidade de Cursos por Instituição: A análise revela que algumas instituições de ensino superior oferecem um grande número de cursos, enquanto outras têm uma oferta mais limitada. Isso sugere que existem instituições com maior diversidade de opções educacionais, o que pode ser benéfico para os estudantes que desejam escolher entre uma variedade de cursos.\n\nPotencial Impacto na Desigualdade Educacional: A alta concentração de cursos em algumas instituições pode contribuir para a desigualdade educacional. Estudantes que têm acesso a uma variedade de cursos podem ter mais oportunidades de escolha e desenvolvimento, enquanto aqueles em regiões com menos instituições ou opções podem enfrentar desafios adicionais no acesso à educação.''')
pdf.ln(10)

pdf.doc_text('''
5. Analisando a disponibilidade do curso de Medicina por região, considerando a quantidade de instituição por região e em quais cidades este curso está disponível.
Ampla Disponibilidade Geográfica: O curso em análise está disponível em um total de 252 cidades. Isso demonstra uma disseminação relativamente ampla da oferta desse curso em várias regiões do Brasil.
Distribuição por Regiões: A análise por regiões geográficas mostra que o curso é oferecido em todas as cinco regiões do país. As quantidades de cidades que oferecem o curso variam consideravelmente, com a região Sudeste liderando com 100 cidades, seguida pelas regiões Nordeste com 61, Sul com 42, Centro-Oeste com 23 e Norte com 27.
Presença de Instituições por Região: Além disso, a análise mostra a quantidade de instituições de ensino que oferecem o curso em cada região. Mais uma vez, a região Sudeste lidera com 124 instituições, seguida pelas regiões Nordeste com 84, Sul com 52, Norte com 38 e Centro-Oeste com 30.
A desigualdade educacional pode ser agravada quando consideramos que algumas instituições podem oferecer cursos de maior prestígio ou com mais recursos, enquanto outras podem enfrentar dificuldades para manter um padrão de qualidade equivalente. Portanto, é crucial que políticas educacionais se concentrem em promover o acesso igualitário à educação e na melhoria da qualidade do ensino em todas as instituições, independentemente do número de cursos oferecidos. Isso contribuirá para reduzir as disparidades educacionais no Brasil e promover um sistema de ensino mais equitativo.
A discrepância entre o Sudeste e outras regiões pode nos mostrar as implicações no que tange a desigualdade educacional. Estudantes que residem nas regiões com menos cidades e instituições que oferecem o curso podem enfrentar desafios adicionais no acesso a essa oportunidade educacional específica. Isso pode resultar em uma desigualdade de acesso, uma vez que os estudantes de outras regiões podem ter mais dificuldade de encontrar o curso desejado. \nA seguir, apresentamos uma representação visual da análise por meio de um gráfico de pizza''')
pdf.doc_image("grafico_qt_instituicao_por_regiaoMED.png", 25, pdf.get_y() + 12, 170, 80)  # Ajuste a coordenada Y para pdf.get_y() + 10
pdf.ln(105)


pdf.doc_text('''6. Analisando a disponibilidade do curso de Direito por região, considerando a quantidade de instituição por região e em quais cidades este curso está disponível.
Ampla Disponibilidade Geográfica: O curso de Direito está disponível em um total de 706 cidades. Isso demonstra uma disseminação relativamente ampla da oferta desse curso em várias regiões do Brasil.
Distribuição por Regiões: A análise por regiões geográficas mostra que o curso é oferecido em todas as cinco regiões do país. As quantidades de cidades que oferecem o curso variam consideravelmente, com a região SUDESTE liderando com 276 cidades, seguida pelas regiões NORDESTE com 143, SUL com 157, CENTRO-OESTE com 85 e NORTE com 48.
Presença de Instituições por Região: Além disso, a análise mostra a quantidade de instituições de ensino que oferecem o curso de Direito em cada região. Mais uma vez, a região SUDESTE lidera com 604 instituições, seguida pelas regiões NORDESTE com 418, SUL com 254, CENTRO-OESTE com 195 e NORTE com 132.
Essa análise revela que o curso de Direito é amplamente oferecido em todo o Brasil, e novamente com uma presença especialmente forte nas regiões Sudeste e Nordeste. No entanto, é importante observar que a quantidade de cidades e instituições que oferecem o curso varia entre as regiões, o que pode afetar o acesso dos estudantes a essa área de estudo.
Para promover a igualdade de oportunidades educacionais em todo o país, é fundamental que as políticas educacionais considerem estratégias para expandir ainda mais a oferta de cursos, inclusive em regiões com menos opções, garantindo que os estudantes de todas as regiões tenham acesso à educação de qualidade, incluindo o curso de Direito. \nA seguir, apresentamos uma representação visual da análise por meio de um gráfico de pizza''')

pdf.doc_image("grafico_qt_instituicao_por_regiaoDIREITO.png", 25, pdf.get_y() + 12, 170, 80)  # Ajuste a coordenada Y para pdf.get_y() + 10
pdf.ln(105)

pdf.doc_text('''7.Analisando a disponibilidade do curso de SOCIOLOGIA por região, considerando a quantidade de instituição por região e em quais cidades este curso está disponível
\nAmpla Disponibilidade Geográfica: O curso de Sociologia está disponível em um impressionante total de 1.813 cidades em todo o Brasil. Essa ampla disponibilidade demonstra a disseminação abrangente da oferta desse curso em diversas regiões do país, tornando-o acessível a estudantes em muitas localidades.
\nDistribuição por Regiões: A análise por regiões geográficas revela que o curso de Sociologia é oferecido em todas as cinco regiões do Brasil, mostrando sua presença nacional. As quantidades de cidades que oferecem o curso variam, com destaque para a região SUDESTE, que lidera com 625 cidades. A região NORDESTE também apresenta uma oferta significativa, com 475 cidades, seguida pela região SUL com 393, CENTRO-OESTE com 150, NORTE com 189 e uma presença internacional que totaliza 1 cidade.
\nPresença de Instituições por Região: Em relação à quantidade de instituições de ensino que oferecem o curso de Sociologia por região, a região SUDESTE lidera com 29 instituições, seguida pela região SUL com 30, NORDESTE com 20, CENTRO-OESTE com 18, NORTE com 18 e uma presença internacional de 3 instituições.
\nDiversidade e Acesso à Sociologia: A Sociologia é um campo fundamental que ajuda a entender a sociedade e suas complexidades. A ampla disponibilidade desse curso em todo o Brasil é uma oportunidade valiosa para estudantes que desejam explorar essa área. Além disso, a presença do curso em todas as regiões promove a diversidade de perspectivas e experiências no estudo da Sociologia.
\n\nApesar da presença nacional, a quantidade de cidades e instituições que oferecem o curso de Sociologia ainda varia entre as regiões. \nA seguir, apresentamos uma representação visual da análise por meio de um gráfico de pizza. ''')
pdf.doc_image("grafico_qt_instituico_por_regiaoSOCIO.png", 25, pdf.get_y() + 12, 170, 80)  # Ajuste a coordenada Y para pdf.get_y() + 10
pdf.ln(105)

pdf.doc_text(''' \n\n8. Analisa as médias dos percentuais de mestrado e doutorado para cada região em ambos os anos:\nCompreender as diferenças regionais nos percentuais de conclusão desses cursos é essencial para abordar desafios educacionais específicos em cada região. Neste relatório, analisaremos os dados disponíveis para as regiões Centro-Oeste, Nordeste, Norte, Sudeste e Sul, entre os anos 2020 e 2021 com o objetivo de compreender melhor essa disparidade educacional.Analisa a disparidade educacional no Brasil em relação à conclusão de Mestrado e Doutorado nos anos de 2020 e 2021, considerando as cinco regiões do país: Centro-Oeste, Nordeste, Norte, Sudeste e Sul: \n\n\nMestrado (2020-2021): \n- O Nordeste apresentou a maior média de conclusão de Mestrado em ambos os anos; \n- O Sudeste teve a menor média de conclusão de Mestrado em ambos os anos.\n\nDoutorado (2020-2021):
- O Sudeste teve a maior média de conclusão de Doutorado em ambos os anos.\n- O Norte registrou a menor média de conclusão de Doutorado em ambos os anos.
\nO exame dessas informações é crucial para direcionar políticas públicas e investimentos na área educacional. As disparidades regionais nos níveis de mestrado e doutorado apontam para desigualdades no acesso ao ensino superior e nas oportunidades educacionais em todo o país. 
\nA seguir as representações da média percentual de mestrado e doutorado nos anos 2020 e 2021 em gráfico de barras: ''')
pdf.ln(2)


pdf.doc_image("grafico_mestrado20202021.png", 25, 140, 150, 100) 

pdf.ln(140)

pdf.doc_text('''\n\n\n\n''')


pdf.ln(40)
pdf.doc_image("grafico_doutorado20202021.png", 25, 30, 150, 100)

pdf.ln(48)
pdf.doc_text('''Agora, gráfico em barras representando a média percentual de cada região para melhor visualização dos dados''')
pdf.ln(80)


pdf.doc_image("grafico_PERCENTUAL_MESTRADO_DOUTORADO.png", 25,155,150,100)
pdf.doc_text('''

\nA existência dessas disparidades evidencia desafios significativos tanto no acesso quanto na conclusão de cursos de pós-graduação nas diversas regiões do Brasil. Para superá-las, torna-se imprescindível direcionar esforços para o investimento em estratégias que não apenas aprimorem a qualidade do ensino, mas também ampliem a oferta de programas de pós-graduação em todas as localidades do país, almejando, assim, alcançar um patamar de equidade educacional.''')
pdf.ln(10)
pdf.doc_text('''9. Analisa os investimentos públicos diretos em educação por estudante no Brasil entre 2000 e 2018. Os dados foram coletados e consolidados pelo Inep/MEC, apresentando valores nominais em reais (R$1,00):\n
            
             Educação Básica: \n\nTodos os Níveis:\n-Em 2000: R$969 \n-Em 2018: R$8.377\n

             Educação Infantil:
\n- Em 2000: R$1.018\n- Em 2018: R$6.811
             
            Ensino Fundamental:
\n- Em 2000: R$774\n- Em 2018: R$7.229

            Ensino Médio:
\n- Em 2000: R$810\n- Em 2018: R$6.877\n

        Educação Superior:
\n- Em 2000: R$779\n- Em 2018: R$8.003

\nEsses valores representam o investimento público direto por estudante em diferentes níveis da Educação Básica no Brasil, em 2000 e 2018. Houve um aumento significativo ao longo desse período. A análise nos mostrou o seguinte:\n\n-Tendência de Investimento em Educação Básica: \nDurante o período analisado, houve um aumento constante no investimento por estudante na Educação Básica, que inclui a Educação Infantil, Ensino Fundamental e Ensino Médio. Isso é um indicativo positivo do comprometimento do Brasil em melhorar a qualidade da educação fundamental e média. No entanto, é importante destacar que, apesar desse aumento, o país ainda enfrenta desafios significativos em seu sistema educacional.\n\n
- Educação Superior:\nEmbora o Brasil tenha realizado investimentos substanciais na Educação Superior, permanecem preocupações significativas relacionadas à qualidade e acessibilidade. Uma parcela considerável da população brasileira ainda encontra dificuldades em acessar o ensino superior devido a barreiras financeiras e outras questões estruturais. Essas preocupações têm implicações diretas no desenvolvimento social e econômico do país.

\n\n- Qualidade da Educação Básica: Apesar dos contínuos aumentos nos investimentos em educação no Brasil, persistem desafios substanciais na melhoria da qualidade da educação básica. Essas questões críticas incluem altas taxas de evasão escolar, a carência de infraestrutura adequada nas escolas e a necessidade premente de aprimorar a formação e a valorização dos professores. Esses desafios comprometem a oferta de uma educação de qualidade para todos os brasileiros e impactam diretamente no desenvolvimento social e econômico do país. 

\nAnalisar os investimentos em educação é fundamental para avaliar o compromisso de um país com o desenvolvimento de suas futuras gerações. Uma educação de qualidade não apenas melhora a vida dos indivíduos, mas também contribui para o crescimento econômico e o fortalecimento da sociedade como um todo.
\nÉ vital que o Brasil continue a aumentar seus investimentos em educação e, ao mesmo tempo, trabalhe na distribuição equitativa desses recursos para garantir que todas as regiões e grupos sociais tenham acesso igualitário a uma educação de qualidade. Além disso, o foco na melhoria da formação de professores e na qualidade da educação básica deve permanecer como uma prioridade. O aumento do investimento é um passo na direção certa, mas é necessário um esforço contínuo e coordenado para atingir os objetivos de uma educação de qualidade para todos os brasileiros''')
  

pdf.ln(10)


pdf.doc_title("CONCLUSÃO:")
pdf.doc_text('''Os dados e análises apresentados neste relatório lançam luz sobre diversas dimensões da desigualdade educacional no Brasil e apontam para questões cruciais que precisam ser enfrentadas. Primeiramente, a diversidade de instituições de ensino, cursos e níveis de grau oferecidos em todo o país oferece oportunidades significativas aos estudantes, mas também impõe o desafio da tomada de decisões educacionais informadas. Nesse contexto, é fundamental que os estudantes recebam orientação educacional adequada para escolher instituições, cursos e níveis de grau que atendam às suas necessidades e interesses específicos.
\nNo entanto, a análise por categoria administrativa revelou uma predominância de instituições de ensino privadas com fins lucrativos. Isso ressalta a necessidade de equilibrar o mercado educacional para garantir que as instituições públicas desempenhem um papel significativo no acesso à educação de qualidade. É essencial que políticas educacionais e alocação de recursos levem em consideração essa distribuição para promover a equidade.
\nA análise das quantidades de instituições de ensino por região revela desigualdades regionais na infraestrutura educacional do país. A concentração de instituições na região Sudeste, a mais populosa e desenvolvida, levanta preocupações sobre a centralização educacional. Para promover a igualdade de oportunidades, é crucial expandir a oferta de cursos e instituições em regiões com menos opções, garantindo que todos os estudantes, independentemente de sua localização geográfica, tenham acesso à educação de qualidade.
\nA disponibilidade de cursos específicos, como Medicina, Direito e Sociologia, também revelou disparidades regionais. Embora esses cursos sejam amplamente oferecidos, a variação na quantidade de cidades e instituições que os oferecem pode afetar o acesso dos estudantes a essas áreas de estudo. Portanto, é imperativo que políticas educacionais incentivem a expansão desses cursos em todas as regiões, promovendo uma oferta mais equitativa.
\nA análise das médias de conclusão de cursos de mestrado e doutorado mostrou diferenças significativas entre as regiões, destacando a desigualdade no acesso ao ensino superior. Essas disparidades refletem a necessidade de estratégias específicas para abordar os desafios educacionais em cada região e garantir oportunidades iguais para todos os brasileiros.
\nPor fim, a análise dos investimentos públicos diretos em educação demonstrou um aumento notável ao longo do tempo, especialmente na Educação Básica. No entanto, apesar desses investimentos, persistem desafios relacionados à qualidade e acessibilidade da educação superior, que afetam diretamente o desenvolvimento social e econômico do país.
\nDiante dessas análises, a problemática da desigualdade educacional no Brasil está clara: o acesso igualitário à educação de qualidade ainda não é uma realidade para todos os brasileiros.
\nA solução para a desigualdade educacional no Brasil requer uma abordagem abrangente e estratégica que aborde os desafios em várias frentes. O país enfrenta disparidades significativas no acesso à educação e na qualidade do ensino, o que impacta diretamente no desenvolvimento social e econômico.
\nEm primeiro lugar, é crucial aumentar os investimentos em educação e distribuí-los de maneira equitativa. Isso garante que todas as regiões do país e grupos sociais tenham acesso a recursos educacionais adequados. O investimento deve ser direcionado não apenas para o ensino superior, mas também para a Educação Básica, que é a base do sistema educacional.
\nAlém disso, é fundamental expandir a oferta de cursos e instituições em regiões com menos opções. Isso garante igualdade de oportunidades para todos os estudantes, independentemente de onde vivem. A diversificação da oferta educacional também deve ser acompanhada por políticas que promovam a qualidade do ensino, incluindo a formação e valorização dos professores.
\nO apoio à escolha educacional é outra peça-chave. Os estudantes precisam de orientação adequada para tomar decisões informadas sobre sua trajetória acadêmica, especialmente considerando a ampla gama de opções disponíveis. Isso os ajuda a alinhar seus interesses e metas com as oportunidades educacionais disponíveis.
\nPara combater a desigualdade educacional, é imprescindível promover a acessibilidade à educação superior. Isso pode ser alcançado por meio de políticas como programas de bolsas e financiamento estudantil, que reduzem as barreiras financeiras ao ensino superior.
\nPor fim, é necessário desenvolver estratégias regionais específicas que abordem as desigualdades educacionais em cada parte do país. As necessidades e desafios variam de uma região para outra, exigindo abordagens adaptadas às circunstâncias locais.
\nEm resumo, enfrentar a desigualdade educacional no Brasil exige um compromisso contínuo com o investimento em educação, a expansão regional das oportunidades educacionais, o apoio à escolha educacional, a melhoria da qualidade do ensino e a promoção da acessibilidade à educação superior. Somente com uma abordagem abrangente e coordenada será possível construir um sistema educacional mais equitativo e preparar o país para um futuro mais igualitário e próspero.''')

pdf.ln(10)
pdf.doc_title("FONTES DE DADOS EDUCACIONAIS:")
pdf.doc_text('''A análise de dados educacionais apresentada neste relatório baseia-se em uma variedade de fontes confiáveis e amplamente reconhecidas. Essas fontes foram cuidadosamente selecionadas para garantir a precisão e a relevância das informações apresentadas. Abaixo estão as principais fontes de dados utilizadas:

Dados Sobre Instituições de Ensino, Cursos e Graus: Os dados relativos a instituições de ensino, cursos oferecidos e graus acadêmicos foram obtidos a partir de fontes governamentais, com destaque para o Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP) e o Ministério da Educação (MEC). Essas fontes forneceram informações detalhadas sobre as instituições de ensino superior no Brasil.

Investimentos Públicos Diretos em Educação: As informações sobre os investimentos públicos diretos em educação por estudante entre os anos de 2000 e 2018 foram coletadas por meio de relatórios oficiais disponibilizados pelo INEP/MEC. Esses dados são essenciais para compreender o financiamento da educação no país ao longo do tempo.

Dados sobre a Disparidade Educacional em Mestrado e Doutorado: A análise das disparidades regionais na conclusão de cursos de mestrado e doutorado nos anos de 2020 e 2021 se baseou em dados do INEP/MEC, bem como em informações de instituições de pesquisa acadêmica.

Dados sobre Cursos de Medicina, Direito e Sociologia: As informações sobre a disponibilidade desses cursos em diferentes regiões do Brasil foram obtidas a partir de dados fornecidos pelo INEP/MEC. Isso permitiu uma análise detalhada da distribuição desses cursos em nosso país.

Dados sobre a Quantidade de Instituições de Ensino por Região: A análise da quantidade de instituições de ensino superior por região foi baseada nos dados do Censo da Educação Superior do INEP/MEC. Esses dados forneceram uma visão abrangente da infraestrutura educacional no Brasil.

Dados sobre a Quantidade de Cursos por Categoria Administrativa: A quantidade de cursos oferecidos por instituições de ensino superior em diferentes categorias administrativas foi obtida a partir de informações do Censo da Educação Superior do INEP/MEC. Isso permitiu uma análise da diversidade de cursos oferecidos em instituições públicas e privadas.

Gráficos e Imagens: Para visualizar os dados de forma clara e acessível, foram criados gráficos e imagens utilizando ferramentas de software especializadas em visualização de dados. Essas representações visuais auxiliaram na compreensão dos resultados apresentados neste relatório.

Dados de Fontes Internacionais: Em alguns casos, dados de fontes internacionais, como a UNESCO e a OCDE, foram utilizados para fins de comparação e contexto global. Essas fontes são amplamente reconhecidas por suas análises educacionais em nível internacional.

Todas as fontes mencionadas acima foram cuidadosamente avaliadas quanto à sua credibilidade e relevância para a análise realizada neste relatório. Qualquer informação adicional ou fontes específicas utilizadas em análises específicas estão detalhadas nas seções relevantes deste documento.''')
pdf.output("RELATÓRIO.pdf")


