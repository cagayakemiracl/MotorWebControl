using System;
using Android.App;
using Android.Content;
using Android.Runtime;
using Android.Views;
using Android.Widget;
using Android.OS;

namespace MotorWebControl
{
    [Activity (Label = "MotorWebControl", MainLauncher = true)]
    public class MainActivity : Activity
    {
        protected override void OnCreate (Bundle bundle)
        {
            base.OnCreate (bundle);

            SetContentView (Resource.Layout.Main);

            Button openBtn  = FindViewById<Button> (Resource.Id.openBtn);
            Button closeBtn = FindViewById<Button> (Resource.Id.closeBtn);
            Button stopBtn  = FindViewById<Button> (Resource.Id.stopBtn);

            openBtn.Click += async (sender, e) => {
                await GetRequest.Create (1);
            };

            closeBtn.Click += async (sender, e) => {
                await GetRequest.Create (2);
            };

            stopBtn.Click += async (sender, e) => {
                await GetRequest.Create (3);
            };
        }
    }
}
