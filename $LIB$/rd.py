from os import urandom as rd
rdf=lambda mi,ma:mi+ord(rd(1))*(ma-mi+1)/256
rdi=lambda mi,ma:int(rdf(mi,ma))
