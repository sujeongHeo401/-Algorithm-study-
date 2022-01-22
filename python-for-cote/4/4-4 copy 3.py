MATCH (p:Poi)-[:HAS]->(l:Location)
MATCH (p)-[:HAS]->(c:Category)
MATCH (p)-[:HAS]->(f:Feature)
MATCH (p)<-[:LIKE]-(g:Gender)
MATCH (p)<-[:LIKE]-(w:With)
MATCH (p)<-[:LIKE]-(a:Age)
with ["성동/성수"] as loc_list, l, c, f, g, w, a, p
unwind loc_list as loc
with l, c, f, g, w, a, p
WHERE l.locationName = loc
with ["카페"] as category_list, c, f, g, w, a, p
unwind category_list as category
with c, f, g, w, a, p
WHERE c.categoryName = category
# WITH  c, f, g, w, a, p
# OPTIONAL MATCH (c1:Category)
# WHERE c1.community = c.community
with ["심플한","편안한","분위기","친절한","소박한","모던한","독특한","고급스러운"] as feat_list, f, g, w, a, p
unwind feat_list as feat
with f, g, w, a, p
WHERE f.featureName = feat
with f, g, w, a, p
OPTIONAL MATCH (f1:Feature)
WHERE f1.community = f.community
with ["여자", "남자"] as gender_list, g, w, a, p
unwind gender_list as gender
with  g, w, a, p
WHERE g.genderName = gender
with ["배우자"] as with_list,  w, a, p
unwind with_list as with
with  w, a, p

WHERE w.withName = with
with ["20대"] as age_list, a, p
unwind age_list as age
with a, p
WHERE a.ageName = age
return distinct p, count(p) limit 30


