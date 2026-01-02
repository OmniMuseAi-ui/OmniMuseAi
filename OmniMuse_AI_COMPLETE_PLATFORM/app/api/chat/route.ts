export async function POST(req){
  const body = await req.json();
  return Response.json({response:'AI response', model:'auto'})
}
