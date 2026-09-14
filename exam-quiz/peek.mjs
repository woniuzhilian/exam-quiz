import fs from 'fs';
const qs=JSON.parse(fs.readFileSync('src/data/questions.json','utf8'));
for(const id of [3,6,257,7]){
  const q=qs.find(x=>x.id===id);
  console.log('==== id',id,'====');
  console.log('Q:',q.question);
  console.log('A:',q.A);
  console.log('B:',q.B);
  console.log('C:',q.C);
  console.log('D:',q.D);
  console.log();
}
