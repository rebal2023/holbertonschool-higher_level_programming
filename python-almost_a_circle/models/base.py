class Base:
   """                                                                                                                                                                                         
   Base class to manage id attribute in all your future classes and to avoid duplicating the same code                                                                                         
   """

   __nb_objects = 0

   def __init__(self, id=None):
       """                                                                                                                                                                                     
       Constructor that assigns a unique id to each object                                                                                                                                     
       """
       if id is None:
           Base.__nb_objects += 1
           self.id = Base.__nb_objects
       else:
           self.id = id
