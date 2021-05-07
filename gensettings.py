gensettingstf = [{
	"uitype": "slider",
	"unit": "float",
	"label": "Temperature",
	"id": "settemp", 
	"min": 0.1,
	"max": 2.0,
	"step": 0.05,
	"default": 1.0,
    "tooltip": "Randomness of sampling. High values can increase creativity but may make text less sensible. Lower values will make text more predictable but can become repetitious."
	},
	{
	"uitype": "slider",
	"unit": "float",
	"label": "Top p Sampling",
	"id": "settopp", 
	"min": 0.1,
	"max": 1.0,
	"step": 0.05,
	"default": 1.0,
    "tooltip": "Used to discard unlikely text in the sampling process. Lower values will make text more predictable but can become repetitious."
	},
	{
	"uitype": "slider",
	"unit": "float",
	"label": "Repetition Penalty",
	"id": "setreppen", 
	"min": 1.0,
	"max": 2.0,
	"step": 0.05,
	"default": 1.0,
    "tooltip": "Used to penalize words that were already generated or belong to the context"
	},
	{
	"uitype": "slider",
	"unit": "int",
	"label": "Amount to Generate",
	"id": "setoutput", 
	"min": 10,
	"max": 500,
	"step": 2,
	"default": 60,
    "tooltip": "Number of tokens the AI should generate. Higher numbers will take longer to generate."
	},
    {
	"uitype": "slider",
	"unit": "int",
	"label": "Max Tokens",
	"id": "settknmax", 
	"min": 512,
	"max": 2048,
	"step": 8,
	"default": 1024,
    "tooltip": "Number of tokens of context to submit to the AI for sampling."
	}]

gensettingsik =[{
	"uitype": "slider",
	"unit": "float",
	"label": "Temperature",
	"id": "settemp", 
	"min": 0.1,
	"max": 2.0,
	"step": 0.05,
	"default": 1.0,
    "tooltip": "Randomness of sampling. High values can increase creativity but may make text less sensible. Lower values will make text more predictable but can become repetitious."
	},
	{
	"uitype": "slider",
	"unit": "float",
	"label": "Top p Sampling",
	"id": "settopp", 
	"min": 0.1,
	"max": 1.0,
	"step": 0.05,
	"default": 1.0,
    "tooltip": "Used to discard unlikely text in the sampling process. Lower values will make text more predictable but can become repetitious."
	},
    {
	"uitype": "slider",
	"unit": "int",
	"label": "Amount to Generate",
	"id": "setikgen", 
	"min": 50,
	"max": 3000,
	"step": 2,
	"default": 200,
    "tooltip": "Number of characters the AI should generate."
	}]