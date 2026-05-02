# select count(ID)
# from FISH_INFO fi
# left join FISH_NAME_INFO fn 
# on fi.FISH_TYPE = fn.FISH_TYPE
# where fn.FISH_NAME in ('BASS', 'SNAPPER');

# select count(id)
# from fish_info
# where fish_type in 
#     (
#         select fish_type
#         from FISH_NAME_INFO 
#         where FISH_NAME in ('BASS', 'SNAPPER')
#     );

select count(id) as FISH_COUNT
from fish_info fi
where exists(
    select id
    from fish_name_info fn
    where fi.fish_type = fn.fish_type and fn.fish_name in ('BASS', 'SNAPPER')
);