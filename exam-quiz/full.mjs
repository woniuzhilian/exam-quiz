import fs from 'fs';
const qs=JSON.parse(fs.readFileSync('src/data/questions.json','utf8'));
for(const id of [306,447,538,658,1588,1626,2002,813,928]){
  const q=qs.find(x=>x.id===id);
  console.log('================ id',id,'================');
  for(const f of ['question','A','B','C','D','analysis','answer']){
    console.log(`[${f}] ${JSON.stringify(q[f])}`);
  }
  console.log();
}
