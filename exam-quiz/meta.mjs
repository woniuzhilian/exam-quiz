import fs from 'fs';
const qs=JSON.parse(fs.readFileSync('src/data/questions.json','utf8'));
const FIELDS=['A','B','C','D'];
const emptyIds=[306,447,448,538,546,568,658,666,669,693,784,813,904,908,928,932,1040,1050,1053,1147,1160,1262,1292,1588,1626,2002];
const extra=[1987,1988,1888,840,694,815,1175,94,451,560,561,682,695,1151,1155,1218,1391,1680,1932];
const ids=[...new Set([...emptyIds,...extra])];
for(const id of ids){
  const q=qs.find(x=>x.id===id); if(!q){console.log(id,'MISSING');continue;}
  const empt=FIELDS.filter(f=>!String(q[f]||'').trim()).join('');
  console.log(`id${q.id} ${q.bigSubject} ${q.year}-${q.yearQnum} [${q.smallSubject}] emptyOpts=${empt||'-'}`);
  console.log(`   Q: ${String(q.question).slice(0,110)}`);
}
