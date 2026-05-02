select count(ID)
from FISH_INFO fi
left join FISH_NAME_INFO fn 
on fi.FISH_TYPE = fn.FISH_TYPE
where fn.FISH_NAME in ('BASS', 'SNAPPER');
