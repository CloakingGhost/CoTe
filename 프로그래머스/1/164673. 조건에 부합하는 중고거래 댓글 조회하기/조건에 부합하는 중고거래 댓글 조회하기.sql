-- 코드를 입력하세요
SELECT b.title, b.board_id, r.REPLY_ID, r.writer_id, r.contents, r.created_date
from USED_GOODS_BOARD b
join USED_GOODS_REPLY r
on b.BOARD_ID = r.BOARD_ID
where b.CREATED_DATE between date('2022-10-00') and date('2022-11-00')


order by r.CREATED_DATE asc, b.TITLE