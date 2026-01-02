export function optimize(p,plan){if(plan==='free')return 'gpt4o-mini';return p.length<500?'deepseek':'gpt4'}
