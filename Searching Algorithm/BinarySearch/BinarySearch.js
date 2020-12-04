binarySearchOneline=(n,l,t=0)=>{a=parseInt(l.length/2);if(!l.includes(n))return null;if(l[a]<n)return binarySearchOneline(n,l.slice(a),a+t);else if(l[a]>n)return binarySearchOneline(n,l.slice(0,a),t);else return t+a;}
binarySearchOneline1=(n,,l,t=0)=>{a=parseInt(l.length/2);return!l.includes(n)?null:l[a]<n?binarySearchOneline1(n,l.slice(a),a+t):l[a]>n?binarySearchOneline1(n,l.slice(0,a),t):t+a;}

function binarySearchBeautify(n, l, t=0) {
  a = parseInt(l.length/2);
  if (!l.includes(n)) return null;
  if (l[a]<n) return binarySearchBeautify(n,l.slice(a),a+t);
  else if (l[a]>n) return binarySearchBeautify(n,l.slice(0,a),t);
  else return t+a;
}
