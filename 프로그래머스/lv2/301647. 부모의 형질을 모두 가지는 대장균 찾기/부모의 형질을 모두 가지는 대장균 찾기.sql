-- 코드를 작성해주세요
select b.id, b.GENOTYPE as GENOTYPE, a.GENOTYPE as PARENT_GENOTYPE
from ECOLI_DATA a
join ECOLI_DATA b
on a.id = b.PARENT_ID
where a.GENOTYPE & b.GENOTYPE = a.GENOTYPE
order by b.id