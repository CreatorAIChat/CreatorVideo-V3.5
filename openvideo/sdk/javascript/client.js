export class VideoClient {
 constructor(baseUrl="http://127.0.0.1:8000",apiKey=null){this.baseUrl=baseUrl.replace(/\/$/,"");this.apiKey=apiKey;}
 async generate(body){const h={"Content-Type":"application/json"};if(this.apiKey)h.Authorization=`Bearer ${this.apiKey}`;
 const r=await fetch(`${this.baseUrl}/v1/videos`,{method:"POST",headers:h,body:JSON.stringify(body)});
 if(!r.ok)throw new Error(await r.text());return await r.json();}
}
