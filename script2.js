function palindrome(MyString){
    var input= MyString.replace(/[^A-Z0-9]/ig, "").toLowerCase();
    var reversedInput= input.split('').reverse().join('');
    if (input=== reversedInput){
       document.write ("<div> " + MyString + "is a palindrome <div>")
    }
    else{
        document.write("<div> " + MyString + "is  not a palindrome <div>")
    }
}
palindrome ("madam")