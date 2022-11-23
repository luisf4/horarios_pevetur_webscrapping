import docx
# import aspose.words as aw

# doc = aw.Document("arquivo.pdf")
# doc.save("out.docx")

doc = docx.Document('out.docx')

lista_cidade = [
   
]

lista_dias = [
   'SEGUNDAASEXTA-FEIRA',
   'SEGUNDAASEXTA-FEIRA',
   'DOMINGOSEFERIADOS',
   'DOMINGOEFERIADOS',
   'SÁBADO',
   'SÁBADOS',
]


for i in doc.paragraphs:


   linha= " ".join((i.text).strip().replace(" ","").split())

   if linha != '':
      if linha in lista_dias:
         pass
      else: 
         print(linha)


   else:
      pass



