const Discord = require('discord.js');
const path = require('path');
const commando = require('discord.js-commando')
const search = require('youtube-search');
const client = new Discord.Client();
//const dirconfig = require(path.join(__dirname, 'config', 'config.json'))
const clientconfig = new commando.CommandoClient({
    owner: process.env.ownerId,
    commandPrefix: process.env.prefix
}); 
const opts = {
    maxResults: 25,
    key: config.youtube_api,
    type: 'video'
};

const fs = require('fs');
const { description } = require('./commands/ping');

client.commands = new Discord.Collection();

const commandFiles = fs.readdirSync('./commands/').filter(file => file.endsWith('.js'));
for(const file of commandFiles){
    const command = require(`./commands/${file}`)

    client.commands.set(command.name, command);
}

client.once('ready', () => {
    client.user.setStatus('idle')
    client.user.setActivity('-search, command new!')
    console.log("Youtuber bot is now online!");
});

client.on('message', async message =>{
    if(message.author.bot) return;
    if(!message.content.startsWith(commandPrefix) || message.author.bot) return;

    const args = message.content.slice(commandPrefix.length).split(/ +/);
    const command = args.shift().toLowerCase();

    if(command === 'ping'){
        client.commands.get('ping').execute(message, args);
    }else if(command === 'youtube'){
        client.commands.get('youtube').execute(message, args);
    }else if(command === 'search'){
        let embed = new Discord.MessageEmbed()
            .setColor("#73ffdc")
            .setDescription("Please enter a search query. Remember to narrow down your search!")
            .setTitle("Youtube Video Search")
            .setThumbnail('https://cdn.havecamerawilltravel.com/photographer/files/2020/01/youtube-logo-new-1068x510.jpg')
            .setTimestamp();
        let embedMsg = await message.channel.send(embed);
        let filter = m => m.author.id === message.author.id;
        let query = await message.channel.awaitMessages(filter, { max: 1 });
        let results = await search(query.first().content, opts).catch(err => console.log(err));
        if(results) {
            let youtubeResults = results.results;
            let i  =0;
            let titles = youtubeResults.map(result => {
                i++;
                return i + ") " + result.title;
            });
            message.channel.send({
                embed: {
                    title: 'Your results!',
                    color: '#0bfc03',
                    description: titles.join("\n")
                }
            }).catch(err => console.log(err));

            filter = m => (m.author.id === message.author.id) && m.content >= 1 && m.content <= youtubeResults.length;
            let collected = await message.channel.awaitMessages(filter, { maxMathces: 1 });
        }
    }
});

client.login(process.env.TOKEN)