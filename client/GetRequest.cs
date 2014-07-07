using System;
using System.Net;
using System.IO;
using System.Threading.Tasks;

namespace MotorWebControl
{
    public static class GetRequest
    {
        static string url_str_base = "http://192.168.11.19:8000?status=";

        async public static Task<string> Create (int status)
        {
            string url_str = string.Concat (url_str_base, status.ToString ());
            WebRequest webRequest = WebRequest.Create (url_str);
            Console.WriteLine (url_str);
            string responseData = string.Empty;

            using (WebResponse response = await webRequest.GetResponseAsync ())
            using (Stream responseStream = response.GetResponseStream ())
            using (StreamReader responseReader = new StreamReader (responseStream)) {
                responseData = await responseReader.ReadToEndAsync ();
            }

            Console.WriteLine (responseData);
            return responseData;
        }
    }
}
