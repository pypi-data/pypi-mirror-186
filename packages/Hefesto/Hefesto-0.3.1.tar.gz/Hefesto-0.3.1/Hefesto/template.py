
class Template:

  template_model = dict(

    Birthdate = dict(
      processURI = "http://purl.obolibrary.org/obo/NCIT_C142470",
      outputURI = "http://www.ebi.ac.uk/efo/EFO_0006921",
      attributeURI = "http://purl.obolibrary.org/obo/NCIT_C68615",
      valueAttributeIRI = None,
      valueOutput= None,
      datatype = "xsd:date",
      startdate = None,
      enddate = None,
      pid = None,
      context_id = None
    ),


    Sex = dict( 
      processURI = "http://purl.obolibrary.org/obo/NCIT_C142470",
      outputURI = "http://purl.obolibrary.org/obo/NCIT_C103159",
      attributeURI = "http://purl.obolibrary.org/obo/NCIT_C28421",
      valueAttributeIRI = None,
      valueOutput= None,
      datatype = "xsd:string",
      startdate = None,
      enddate = None,
      pid = None,
      context_id = None
    ),


    Status = dict(
      processURI= "http://purl.obolibrary.org/obo/NCIT_C142470",
      outputURI= "http://purl.obolibrary.org/obo/NCIT_C103159",
      attributeURI= "http://purl.obolibrary.org/obo/NCIT_C166244",
      valueAttributeIRI = None,
      valueOutput= None,
      datatype = "xsd:string",
      startdate = None,
      enddate = None,
      pid = None,
      context_id = None
    ),

    Date_of_death = dict( 
      processURI= "http://purl.obolibrary.org/obo/NCIT_C142470",
      outputURI= "http://purl.obolibrary.org/obo/NCIT_C103159",
      attributeURI= "http://purl.obolibrary.org/obo/NCIT_C70810",
      valueAttributeIRI = None,
      valueOutput= None,
      datatype = "xsd:date",
      startdate = None,
      enddate = None,
      pid = None,
      context_id = None
    ),

    Care_pathway = dict(
      processURI= "http://purl.obolibrary.org/obo/NCIT_C159705",
      outputURI= "http://purl.obolibrary.org/obo/NCIT_C25716",
      attributeURI= "http://purl.obolibrary.org/obo/NCIT_C164021",
      valueAttributeIRI = None,
      valueOutput= None,
      datatype = "xsd:date",
      startdate = None,
      enddate = None,
      pid = None,
      context_id = None
    ),

    Diagnosis = dict(
      processURI= "http://purl.obolibrary.org/obo/NCIT_C15220",
      outputURI= "http://purl.obolibrary.org/obo/NCIT_C103159",
      attributeURI= "http://purl.obolibrary.org/obo/NCIT_C2991",
      valueAttributeIRI = None,
      valueOutput= None,
      datatype = "xsd:string",
      startdate = None,
      enddate = None,
      pid = None,
      context_id = None
    ),

    Onset_diagnosis = dict(
      processURI= "http://purl.obolibrary.org/obo/NCIT_C142470",
      outputURI = "http://purl.obolibrary.org/obo/NCIT_C103159",
      attributeURI= "http://purl.obolibrary.org/obo/NCIT_C156420",
      valueAttributeIRI = None,
      valueOutput= None,
      datatype = "xsd:date",
      startdate = None,
      enddate = None,
      pid = None,
      context_id = None
    ),

    Onset_symptoms = dict(
      processURI= "http://purl.obolibrary.org/obo/NCIT_C142470",
      outputURI = "http://purl.obolibrary.org/obo/NCIT_C103159",
      attributeURI= "http://purl.obolibrary.org/obo/NCIT_C124353",
      valueAttributeIRI = None,
      valueOutput= None,
      datatype = "xsd:date",
      startdate = None,
      enddate = None,
      pid = None,
      context_id = None
    ),

    Phenotype = dict(
      processURI= "http://purl.obolibrary.org/obo/NCIT_C25305",
      outputURI= "http://purl.obolibrary.org/obo/NCIT_C125204",
      attributeURI= "http://semanticscience.org/resource/SIO_010056",
      valueAttributeIRI = None,
      valueOutput= None,
      datatype = "xsd:date",
      startdate = None,
      enddate = None,
      pid = None,
      context_id = None
    ),

    Genotype_HGVS = dict(
      processURI= "http://purl.obolibrary.org/obo/NCIT_C15709",
      outputURI= "http://purl.obolibrary.org/obo/NCIT_C17248",
      attributeURI= "http://edamontology.org/data_2127",
      valueAttributeIRI = None,
      valueOutput= None,
      datatype = "xsd:string",
      startdate = None,
      enddate = None,
      pid = None,
      context_id = None
    ),

    Genotype_OMIM = dict(
      processURI= "http://purl.obolibrary.org/obo/NCIT_C15709",
      outputURI= "http://purl.obolibrary.org/obo/NCIT_C16612",
      attributeURI= "http://edamontology.org/data_1153",
      valueAttributeIRI = None,
      valueOutput= None,
      datatype = "xsd:string",
      startdate = None,
      enddate = None,
      pid = None,
      context_id = None
    ),

    Genotype_HGNC = dict(
      processURI= "http://purl.obolibrary.org/obo/NCIT_C15709",
      outputURI= "http://purl.obolibrary.org/obo/NCIT_C16612",
      attributeURI= "http://edamontology.org/data_2298",
      valueAttributeIRI = None,
      valueOutput= None,
      datatype = "xsd:string",
      startdate = None,
      enddate = None,
      pid = None,
      context_id = None
    ),

    Consent = dict(
      processURI= "http://purl.obolibrary.org/obo/OBI_0000810",
      outputURI = None,
      attributeURI= "http://purl.obolibrary.org/obo/NCIT_C25460",
      valueAttributeIRI = None,
      valueOutput= None,
      datatype = "xsd:string",
      startdate = None,
      enddate = None,
      pid = None,
      context_id = None
    ),

    Biobank = dict(
      processURI= "http://purl.obolibrary.org/obo/OMIABIS_0000061",
      outputURI= "http://purl.obolibrary.org/obo/NCIT_C115570",
      attributeURI= "http://purl.obolibrary.org/obo/NCIT_C25429",
      valueAttributeIRI = None,
      valueOutput= None,
      datatype = "xsd:string",
      startdate = None,
      enddate = None,
      pid = None,
      context_id = None
    ),

    Disability = dict(
      processURI = None,
      outputURI= "http://purl.obolibrary.org/obo/NCIT_C25338",
      attributeURI= "http://purl.obolibrary.org/obo/NCIT_C21007",
      valueAttributeIRI = None,
      valueOutput= None,
      datatype = "xsd:float",
      startdate = None,
      enddate = None,
      pid = None,
      context_id = None
    ),

    Body_measurement = dict(
      processURI = None ,
      outputURI=  "http://purl.obolibrary.org/obo/NCIT_C93940" ,
      inputURI= None ,
      inputLabel= None ,
      targetURI= None ,
      targetLabel= None ,
      attributeURI= None ,
      valueOutput= None ,
      datatype= "xsd:float" ,
      valueAttributeIRI= None ,
      unitURI= None ,
      unitLabel= None ,
      model= "Body_measurement" ,
      startdate= None ,
      enddate= None ,
      comments= None ,
      pid= None ,
      context_id= None 
    ),


    Lab_measurement = dict(
      processURI = None ,
      outputURI=  "http://purl.obolibrary.org/obo/NCIT_C93940" ,
      inputURI= None ,
      inputLabel= None ,
      targetURI= None ,
      targetLabel= None ,
      attributeURI= "http://purl.obolibrary.org/obo/NCIT_C134032" ,
      valueOutput= None ,
      datatype= "xsd:float" ,
      valueAttributeIRI= None ,
      unitURI= None ,
      unitLabel= None ,
      model= "Lab_measurement" ,
      startdate= None ,
      enddate= None ,
      comments= None ,
      pid= None ,
      context_id= None 
    ),


    Imaging = dict(
      processURI = None ,
      outputURI=  "http://purl.obolibrary.org/obo/NCIT_C19477" ,
      inputURI= None ,
      inputLabel= None ,
      targetURI= None ,
      targetLabel= None ,
      attributeURI= "http://purl.obolibrary.org/obo/NCIT_C94607" ,
      valueOutput= None ,
      datatype= "xsd:string" ,
      valueAttributeIRI= None ,
      unitURI= None ,
      unitLabel= None ,
      model= "Imaging" ,
      startdate= None ,
      enddate= None ,
      comments= None ,
      pid = None ,
      context_id= None 
    ),


    Treatment = dict(
      processURI = None ,
      outputURI =  None ,
      inputURI = None ,
      inputLabel = None ,
      targetURI = None ,
      targetLabel = None ,
      attributeURI = "http://purl.obolibrary.org/obo/NCIT_C25178" ,
      valueOutput = None ,
      datatype = "xsd:string" ,
      valueAttributeIRI = None ,
      unitURI = None ,
      unitLabel = None ,
      model = "Treatment" ,
      startdate= None ,
      enddate= None ,
      comments= None ,
      pid= None ,
      context_id= None 
    ),


    Clinical_trials = dict(
      processURI = "http://purl.obolibrary.org/obo/NCIT_C71104" ,
      outputURI=  "http://purl.obolibrary.org/obo/NCIT_C115575" ,
      inputURI= "http://purl.obolibrary.org/obo/NCIT_C16696" ,
      inputLabel= None ,
      targetURI= None ,
      targetLabel= None ,
      attributeURI= "http://purl.obolibrary.org/obo/NCIT_C2991" ,
      valueOutput= None ,
      datatype= "xsd:string" ,
      valueAttributeIRI= None ,
      unitURI= None ,
      unitLabel= None ,
      model= "Clinical_trials" ,
      startdate= None ,
      enddate= None ,
      comments= None ,
      pid= None ,
      context_id= None 
    ),


    Medications = dict(
      processURI = "http://purl.obolibrary.org/obo/NCIT_C25538",
      outputURI =  None ,
      inputURI = None ,
      inputLabel = None ,
      targetURI = None ,
      targetLabel = None ,
      attributeURI = None ,
      valueOutput = None ,
      datatype = "xsd:float" ,
      valueAttributeIRI= None ,
      unitURI = None ,
      unitLabel = None ,
      model= "Medications" ,
      atcURI = None,
      frequencyURI = None,
      frequencyLabel = None,
      valueFrequency = None,
      startdate= None ,
      enddate = None ,
      comments = None ,
      pid = None ,
      context_id = None 
    ),


  )

