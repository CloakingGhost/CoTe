-- 코드를 입력하세요
SELECT BOOK_ID, date_format(published_date,'%Y-%m-%d') PUBLISHED_DATE from book where CATEGORY = '인문' and year(PUBLISHED_DATE) = 2021 order by PUBLISHED_DATE asc;