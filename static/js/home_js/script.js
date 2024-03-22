const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnLogin-popup');
const iconClose = document.querySelector('.icon-close');

registerLink.addEventListener('click',()=>{
    wrapper.classList.add('active');
});

loginLink.addEventListener('click',()=>{
    wrapper.classList.remove('active');
});

btnPopup.addEventListener('click',()=>{
    wrapper.classList.add('active-popup');
});

iconClose.addEventListener('click',()=>{
    wrapper.classList.remove('active-popup');
});


window.onload = function(){
    var first = document.getElementById('user_type')
    var second = document.getElementsByClassName('date')

}

for( var x in subjectObject){
    console.log(x)
}











var subjectObject = {
    "Front-End": {
      "HTML": ["Tags", "Links", "Images", "Tables", "Lists", "colors", "Attributes", "Classes", "input", "Iframes", "Div/Span", "Metatags", "Headings", "Favions"],
      "CSS": ["padding", "Margins", "Borders", "Display", 'Icons', "Units", 'z-index', 'Pseudo-class', "Pseudo-element", "!important", "Text-Effect", "Mart-Function", "Transitions", "Aminations", "Transform", "Variables", "Flexbox", 'Grid', 'Masking', 'Media Query'],
      "Bootstrap5": ['Accordion', 'Tooltips', 'Toasts', 'Navs & tabs', 'Carousel', 'Collapse', 'Alerts', 'Badge', 'Card', 'List group', 'Navbar', 'Pagination', 'Progress', 'Scrollspy', 'Spinners', ],
      "JavaScript": ["Variables", "Operators", "Functions", "Conditions", "Loops", "Array", "Object", "DOM", "Local-Storage", "API", "ES6"],
      "React.JS": ['Components', 'JSX', 'State', 'Props', 'Lists & Keys', 'Styling', 'Life Cycle Method', 'Hooks', 'Form Handling', 'Data Handling', 'Custom Hooks', 'Contet', 'portals', 'Routing', 'State Management', 'Patterns', 'Anti-Patterns']
    },
    "Back-end": {
      "Express.js": ['Routing and HTTP Methods', 'Middleware', 'Cookies', 'REST APIs', 'Scaffolding', 'Database Connectivity', 'Templating'],
      "Node.js": ['REPL', 'package manager', 'callbacks', 'event loop', 'os', 'path', 'query string', 'cryptography', 'debugger', 'URL', 'DNS', 'Net', 'UDP', 'process', 'child processes', 'buffers', 'streams', 'file systems', 'global objects', 'web modules']
    },
    "Database":{
      "MongoDB" : ['Documents', 'Collections', 'Compass', 'Replica Sets', 'Sharding', 'Indexes', 'Aggregation Pipelines', 'MongoDB Cloud'],
      "MySQL" : ['Create TABLE', 'Insert Data Into Table', 'Select Query', 'Table Constraints', 'And oR and NOT Operator', 'IN Operator', 'LIKE Operator', 'MySQL Aggregate Functions'],
    },
    "Hybrid/Cross-Platform":{
      "Electron JS": ['Main and Renderer Process', 'Browser Window', 'Quote Widget', 'IPC', 'Application Menu', 'Context Menu', 'Accelerators', 'Shell Module', 'Tray Module', 'CRUD File'],
      "React-Native": ['React Native CLI', 'Ejecting Expo', 'State Hook', 'Styles & Style Sheet', 'List, ScrollView & RefreshControl', 'Alert & Toast Message'],
      "NativeScript": []
    }
}