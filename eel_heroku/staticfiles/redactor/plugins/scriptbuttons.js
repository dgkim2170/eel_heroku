(function($)
{
    $.Redactor.prototype.scriptbuttons = function()
    {
        return {
            init: function()
            {
                // var sup = this.button.add('x²', 'superscript');
                // var sub = this.button.add('x₂', 'subscript');
                var sup = this.button.add('gallery', 'superscript');
                var sub = this.button.add('gallery', 'subscript');
                // var sup = this.button.add('star', 'x&sup2;');
                // var sub = this.button.add('star', 'x&sup2;');
 
                this.button.addCallback(sup, this.scriptbuttons.formatSup);
                this.button.addCallback(sub, this.scriptbuttons.formatSub);
            },
            formatSup: function()
            {
                this.inline.format('sup');
            },
            formatSub: function()
            {
                this.inline.format('sub');
            }
        };
    };
})(jQuery);
 
(function()
{
    $('#redactor').redactor({
        plugins: ['scriptbuttons']
    });
});